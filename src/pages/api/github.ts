// GitHub 提交代理：让博客在没有 CMS 的情况下也能"在网页里写博客"。
// 前端（/write、旅程记录等）把文件内容 POST 到这里，本函数用 Contents API 提交，
// Vercel 检测到 main 分支新变化后自动重新部署，约 1 分钟后内容上线。
//
// 配置（Vercel → Settings → Environment Variables）：
//   GITHUB_TOKEN  —— github.com/settings/tokens 生成，勾选 repo 权限
//   GITHUB_REPO   —— 缺省 pengjinrui278/xixiblog
// 未配置时 GET /api/github 返回 enabled:false，前端自动降级为
// "生成 Markdown 给你复制保存"，功能不缺席。

export const prerender = false;

const REPO = process.env.GITHUB_REPO ?? 'pengjinrui278/xixiblog';
const TOKEN = process.env.GITHUB_TOKEN ?? '';
const BRANCH = 'main';
const API = `https://api.github.com/repos/${REPO}/contents`;

interface FilePayload {
  path: string;           // 仓库内路径，如 src/content/trips/hangzhou.md
  content: string;        // utf8 文本或 base64
  encoding: 'utf8' | 'base64';
}

async function putFile(f: FilePayload, message: string) {
  const existing = await fetch(`${API}/${f.path}?ref=${BRANCH}`, {
    headers: { Authorization: `Bearer ${TOKEN}`, 'User-Agent': 'xixi-blog' },
  });
  const sha = existing.ok ? (await existing.json()).sha : undefined;

  const body: any = {
    message,
    branch: BRANCH,
    content: f.encoding === 'base64' ? f.content : Buffer.from(f.content, 'utf8').toString('base64'),
  };
  if (sha) body.sha = sha;

  const r = await fetch(`${API}/${f.path}`, {
    method: 'PUT',
    headers: { Authorization: `Bearer ${TOKEN}`, 'User-Agent': 'xixi-blog', 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw new Error(`${f.path}: GitHub ${r.status} ${(await r.text()).slice(0, 200)}`);
  return f.path;
}

async function delFile(path: string, message: string) {
  const existing = await fetch(`${API}/${path}?ref=${BRANCH}`, {
    headers: { Authorization: `Bearer ${TOKEN}`, 'User-Agent': 'xixi-blog' },
  });
  if (!existing.ok) throw new Error(`${path}: GitHub ${existing.status}（文件不存在？）`);
  const { sha } = await existing.json();
  const r = await fetch(`${API}/${path}`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${TOKEN}`, 'User-Agent': 'xixi-blog', 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, branch: BRANCH, sha }),
  });
  if (!r.ok) throw new Error(`${path}: GitHub ${r.status} ${(await r.text()).slice(0, 200)}`);
  return path;
}

// 防路径穿越：只允许白名单目录（新增与删除共用）
const PATH_RE = /^(src\/content\/(posts|trips|movies|memos|days)\/[\w\-.一-龥]+\.(md|markdown)|public\/photos\/[\w\-.]+\.(svg|png|jpe?g|webp|gif))$/;

export async function GET() {
  return Response.json({ enabled: Boolean(TOKEN), repo: REPO, branch: BRANCH });
}

export async function POST({ request }: { request: Request }) {
  if (!TOKEN) return Response.json({ error: 'GITHUB_TOKEN 未配置', code: 'no-token' }, { status: 501 });
  try {
    const { files, deletions, message } = await request.json();
    const done: string[] = [];
    if (Array.isArray(files)) {
      if (files.length === 0 || files.length > 10) {
        return Response.json({ error: 'files 须为 1-10 项的数组' }, { status: 400 });
      }
      for (const f of files as FilePayload[]) {
        if (!PATH_RE.test(f.path)) {
          return Response.json({ error: `路径不被允许: ${f.path}` }, { status: 400 });
        }
        done.push(await putFile(f, message ?? `write: ${f.path}`));
      }
    }
    if (Array.isArray(deletions)) {
      if (deletions.length === 0 || deletions.length > 10) {
        return Response.json({ error: 'deletions 须为 1-10 项的数组' }, { status: 400 });
      }
      for (const p of deletions as string[]) {
        if (!PATH_RE.test(p)) {
          return Response.json({ error: `路径不被允许: ${p}` }, { status: 400 });
        }
        done.push(await delFile(p, message ?? `delete: ${p}`));
      }
    }
    if (!done.length) return Response.json({ error: 'files 或 deletions 至少提供一项' }, { status: 400 });
    return Response.json({ ok: true, committed: done });
  } catch (e: any) {
    return Response.json({ error: String(e?.message ?? e) }, { status: 502 });
  }
}
