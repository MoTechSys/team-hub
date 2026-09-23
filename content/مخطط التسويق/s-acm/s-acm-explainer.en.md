s-acm | مخطط التسويق | 2026-09-23 | draft (for editor seal)

# S-ACM — Smart Academic Content Management System

## Executive summary (5 points)
1. An open-code university graduation project that brings academic content (lectures, summaries, exams), users and permissions into one Arabic-first (RTL) web platform.
2. Built as a Turborepo monorepo: a React 19 + TypeScript + Tailwind 4 + shadcn/ui frontend and a Hono backend on PostgreSQL with Drizzle, Zod and JWT.
3. The core feature is a fully dynamic permissions system: 70+ permissions across 12 sections in 3 nested levels; admins compose roles themselves with no code changes.
4. Size as in the repository: 19 frontend pages, 14 API route modules, 13 database tables, 7 functional modules.
5. Status: frontend 95% complete, backend 60%, permissions 40%, AI features planned (0%); live deployment currently down — to be confirmed.

## The problem
On campus, lecture files, summaries and exams end up scattered across chat groups, email and lecturers' laptops. There is no archive, no search, and no structured way to decide who sees what: permissions for students, lecturers and staff are handled by hand, and every semester starts from zero.

## How it works
S-ACM is a fully Arabic (RTL, dark mode) web platform that puts three things in one place:
- Users: registration of students, lecturers and staff with automatic academic IDs, roles and permissions.
- Courses: linked to majors and academic levels, each with its own classified files.
- Files: upload and classification (lecture, summary, exam, reference…) with an in-app viewer, a trash bin and audit logs.

Under the hood it is one monorepo managed with Turborepo and pnpm workspaces: the `apps/web` frontend in React 19, TypeScript, Tailwind CSS 4 and shadcn/ui; the `apps/api` backend on the lightweight Hono framework (Node) with Drizzle ORM over PostgreSQL, Zod for input validation and JWT with bcryptjs for authentication; plus a `packages/shared` package for shared types. Charts use Recharts; builds use Vite 7.

The most important part is permissions: instead of roles hard-coded in the source, the system defines 70+ permissions spread over 12 sections in 3 nested levels, and the administrator can create new roles and compose their permissions from the UI.

## Who it is for
- Graduation-project students who want a real, complete reference for a modern monorepo with dynamic permissions — not a simplified tutorial.
- University departments and faculties looking for a lightweight Arabic starting point for managing teaching content, instead of heavy systems or unmanaged chat groups.

## What sets it apart
Arabic RTL by design rather than translated later; dynamic permissions built by the admin, not the developer; and a current stack (React 19, Tailwind 4, Hono, Drizzle) in an open repository with API and developer documentation — rare among published graduation projects.

## Current status and what remains
Per the repository README: frontend 95% complete, Hono backend 60% in progress, permissions system 40%, and the AI features (content summarisation and question generation) planned but not yet built. The live deployment on Vercel and Railway was down at check time (2026-09-11), so the screenshots in this pack come from a local run of the frontend on seed data (names and figures are not real). Live link and demo video: to be confirmed.

<!-- Sources: 01-projects/s-acm/brief.en.md · tech.md · README moain2028/s-acm (verified 2026-09-23). No figure outside these files. -->
