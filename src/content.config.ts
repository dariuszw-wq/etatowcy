import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const lang = z.enum(['pl', 'en', 'es']);

/** Oferta pracy: src/content/jobs/<lang>/<slug>.md — ten sam slug w trzech językach = ta sama oferta */
const jobs = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/jobs' }),
  schema: z.object({
    lang,
    title: z.string(),
    city: z.string(),
    industry: z.string(),
    contract: z.string(),
    pay: z.string(),
    terms: z.string(),
    tags: z.array(z.string()).max(3).default([]),
    published: z.coerce.date(),
    expires: z.coerce.date().optional(),
    example: z.boolean().default(false),
  }),
});

/** Wiadomość z rynku pracy: src/content/news/<lang>/<slug>.md */
const news = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/news' }),
  schema: z.object({
    lang,
    title: z.string(),
    excerpt: z.string(),
    published: z.coerce.date(),
    readingTime: z.number().int().positive().default(3),
    source: z.string().optional(),
  }),
});

export const collections = { jobs, news };
