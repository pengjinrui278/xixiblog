import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string().nullish(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    // 系列：同名 series 自动聚合、自动排上下篇
    series: z.object({
      name: z.string(),
      order: z.number(),
    }).optional(),
    // 本篇 BGM：歌名 —— 艺术家，点击联动唱片机
    bgm: z.object({
      mid: z.string(),
      name: z.string(),
      artist: z.string(),
    }).optional(),
    draft: z.boolean().default(false),
  }),
});

const trips = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/trips' }),
  schema: z.object({
    title: z.string(),
    // 网页表单可能产出空串/缺键（YAML 解析成 null）——nullish 容忍，绝不让单条坏数据炸掉整站构建
    place: z.string().nullish(),
    // WGS-84 坐标（GPS 原始值），前端展示时转 GCJ-02 对齐高德瓦片
    coords: z.object({ lng: z.number(), lat: z.number() }),
    date: z.coerce.date(),
    photo: z.string().optional(),
    song: z.object({
      mid: z.string(),
      name: z.string(),
      artist: z.string(),
    }).optional(),
    excerpt: z.string().nullish(),
  }),
});

// 观影：票根式极简 frontmatter——字少，一目了然
const movies = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/movies' }),
  schema: z.object({
    title: z.string(),
    year: z.number(),
    rating: z.number().min(0).max(5),
    quote: z.string().max(80),
    // 票根底色（中国传统色），缺省随机
    color: z.string().optional(),
    watchedDate: z.coerce.date().optional(),
  }),
});

// 便签：灵感墙的最小单元
const memos = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/memos' }),
  schema: z.object({
    text: z.string(),
    color: z.string().default('#D9A441'),
    date: z.coerce.date(),
  }),
});

// 特别的日子：'MM-DD' 每年重复（生日/节日），'YYYY-MM-DD' 仅那一年（纪念日）
// ⚠️ frontmatter 里 date 必须加引号——未加引号会被 YAML 解析成 Date 对象
const days = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/days' }),
  schema: z.object({
    title: z.string(),
    date: z.union([z.string(), z.date()]).transform((v) =>
      typeof v === 'string' ? v : v.toISOString().slice(0, 10)),
    color: z.string().optional(),
    note: z.string().optional(),
  }),
});

export const collections = { posts, trips, movies, memos, days };
