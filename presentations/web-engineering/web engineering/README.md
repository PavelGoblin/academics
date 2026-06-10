# 🍪 Cookies & Sessions — Interactive Web Engineering Presentation

[![Live Demo](https://img.shields.io/badge/Live-Demo-0066cc?style=for-the-badge&logo=githubpages&logoColor=white)](https://pavelgoblin.github.io/presentation/)
[![Course](https://img.shields.io/badge/Course-Web%20Engineering-A50044?style=for-the-badge)](#)
[![Author](https://img.shields.io/badge/Author-Mohammad%20Ibrahim-FFCD00?style=for-the-badge)](#)

---

## 📖 Overview

A **high-level interactive single-page presentation** on **Cookies and Sessions** in Web Engineering, covering **5 fundamental questions** about HTTP state management. Built with pure HTML, CSS, and JavaScript — **no frameworks, no dependencies**. Works entirely offline.

**Presented by:** Mohammad Ibrahim  
**Course:** Web Engineering (Chapters 1, 2, 6)  
**Instructor:** Mir Md. Kawsur — Lecturer, Faculty, Dept. of Computer Science | Adjunct Faculty, School of Science & Technology, BOU  
**Date:** June 2026

---
১. Cookie বনাম Session: আর্কিটেকচারাল পার্থক্য
 এদের মূল পার্থক্য হলো Data Location বা ডাটা কোথায় থাকছে তার ওপর [৪, ১৮]।
Cookie: এটি একটি ক্লায়েন্ট-সাইড স্টোরেজ। সার্ভার Set-Cookie হেডারের মাধ্যমে ব্রাউজারকে ডাটা পাঠায় এবং ব্রাউজার সেটি সেভ করে রাখে [২]। এর সাইজ লিমিট মাত্র 4KB এবং এটি সিকিউরিটির দিক থেকে ঝুঁকিপূর্ণ কারণ ইউজার বা জাভাস্ক্রিপ্ট এটি এক্সেস করতে পারে (যদি না HttpOnly ফ্ল্যাগ থাকে) [৪, ৫, ১৮]।
Session: এটি সার্ভার-সাইড স্টোরেজ। আসল ডাটা থাকে সার্ভারের মেমোরিতে (যেমন: Redis বা DB), আর ব্রাউজারে থাকে শুধু একটি Session ID (SID) [২, ৪]।
অ্যানালজি: কুকি হলো একটি লাইব্রেরি কার্ড (সব তথ্য আপনার কার্ডেই লেখা আছে), আর সেশন হলো একটি ব্যাংক লকার (আপনার মূল্যবান জিনিস ব্যাংকের ভল্টে নিরাপদ আছে, আপনার কাছে শুধু লকারের চাবি বা SID আছে) [৩, ৪]।
২. Facebook বনাম Google: স্কেলেবিলিটি এবং কনসিস্টেন্সি
বড় কোম্পানিগুলো কীভাবে বিলিয়ন ইউজারের ডাটা হ্যান্ডেল করে, তার পেছনে দুটি ভিন্ন দর্শন কাজ করে [৬]:
Facebook (Eventual Consistency): ফেসবুক TAO নামক ডিস্ট্রিবিউটেড ডাটা স্টোর ব্যবহার করে [৬, ৮]। তারা Speed-কে প্রাধান্য দেয়। আপনি যখন কিছু পোস্ট করেন, তা সাথে সাথে রাইট হয় কিন্তু বিশ্বের সব ডাটা সেন্টারে তা আপডেট হতে কয়েক সেকেন্ড সময় লাগতে পারে [৮, ৯]। এটাকে বলে Eventual Consistency [৭, ৯]।
Google (Strong Consistency): গুগল Spanner নামক ডাটাবেস ব্যবহার করে যা ACID transactions নিশ্চিত করে [৭, ৮]। ইমেল বা পেমেন্টের মতো কাজের জন্য ডাটা সব সময় নির্ভুল হতে হয়। তাই গুগলের ডাটা সারা বিশ্বে সবসময় Strongly Consistent থাকে, অর্থাৎ নিউইয়র্ক বা ঢাকা—সবখানে আপনি একই ডাটা একই সময়ে দেখবেন [৭, ৮, ৯]।
৩. "Remember Me" ইমপ্লিমেন্টেশন এবং সিকিউরিটি
এটি করার সময় কেবল একটি কুকি সেট করলেই হয় না, প্রপার সিকিউরিটি স্টেপ ফলো করতে হয় [১০]:
ইউজার যখন এটি সিলেক্ট করে, সার্ভার একটি Cryptographically random 256-bit token তৈরি করে [১০]।
Hashing: ডাটাবেসে কখনোই আসল টোকেন সেভ করা যাবে না। টোকেনটিকে SHA-256 দিয়ে হ্যাশ করে রাখতে হবে [১০, ১১]।
Token Rotation: এটি সবচেয়ে গুরুত্বপূর্ণ। ইউজার যখনই ওই টোকেন দিয়ে অটো-লগইন করবে, সার্ভার পুরনো টোকেনটি ডিলিট করে একটি নতুন টোকেন ইস্যু করবে [১০, ১৮]। এতে টোকেন চুরি হলেও হ্যাকার সেটি একবারের বেশি ব্যবহার করতে পারবে না [১১]。
৪. নির্দিষ্ট ডিভাইস থেকে লগআউট (Selective Logout)
প্রফেসরকে বোঝাবেন যে, ব্রাউজার থেকে কুকি ডিলিট করাই যথেষ্ট নয় [১৪]।
Unique SID: প্রতিটি ডিভাইসের (যেমন: মোবাইল, ল্যাপটপ) জন্য সার্ভার আলাদা আলাদা Session ID (SID) জেনারেট করে [১২]।
Server-side Invalidation: যদি কোনো ডিভাইস চুরি হয়ে যায়, ইউজার অন্য ডিভাইস থেকে সেই নির্দিষ্ট SID-টি ডাটাবেস থেকে ডিলিট বা ইনভ্যালিড করে দেয় [১৩]।
কেন? কারণ ডিভাইসটি যদি অফলাইন থাকে, তবে ক্লায়েন্ট-সাইড কুকি ডিলিট করা সম্ভব নয়। একমাত্র সার্ভার-সাইড ডিলিট নিশ্চিত করে যে হ্যাকার আর সেই সেশন ব্যবহার করতে পারবে না [১৪, ১৯]।
৫. থিম সিলেকশন: Cookie না Session?
ইউজারের ডার্ক বা লাইট মোড থিমের জন্য Cookie বা localStorage ব্যবহার করা উচিত, সেশন নয় [১৫, ১৯]।
Persistence: সেশন কুকি ব্রাউজার বন্ধ করলে ডিলিট হয়ে যায়, কিন্তু থিম রিস্টার্টের পরেও টিকে থাকা দরকার (Persistent Cookie) [১৫]।
Performance: সেশনে ডাটা রাখলে প্রতিবার পেজ লোড হওয়ার সময় সার্ভার থেকে ডাটা রিকোয়েস্ট করতে হয়, যা 50-500ms দেরি করতে পারে এবং এতে একটি "Flash of unstyled light mode" দেখা যায় [১৬]। কুকি ব্যবহার করলে ব্রাউজার 1ms-এর কম সময়ে থিম অ্যাপ্লাই করতে পারে [১৬, ১৭]।
থাম্ব রুল: ডাটা যদি সেনসিটিভ না হয় এবং স্পিড দরকার হয়, তবে কুকি ব্যবহার করুন [১৬, ১৯]।

## 🎯 Questions Answered

| # | Question | Summary |
|---|----------|---------|
| **Q1** | What is the visual/architectural difference between a Cookie and a Session? | Cookie = client-side (browser) storage; Session = server-side (Redis/DB) storage. Location determines security, size, lifetime, and blocking behavior. |
| **Q2** | How do Facebook and Google manage billions of sessions and cookies? | Facebook uses **TAO + Memcache** (eventual consistency). Google uses **Spanner + OAuth 2.0** (strong consistency with ACID transactions). |
| **Q3** | How does "Remember Me" work under the hood? | 256-bit random token → SHA-256 hash → DB storage → persistent cookie (30-day) → **mandatory token rotation** on every use. |
| **Q4** | How to log out from a specific device without affecting others? | Each device gets a **unique Session ID**. Server-side deletion of that SID only. Client-only clearing is insufficient. |
| **Q5** | Should dark/light theme preference be stored in a Cookie or Session? | **Cookie or localStorage** — not server session. Non-sensitive, needs persistence, faster client-side. |

---

## ✨ Features

### 🎨 Visual Design
- **Dark premium theme** with glassmorphism (frosted glass cards, backdrop blur)
- **9 color themes** — Barca (default), Midnight, Forest, Sunset, Ocean, Rose, Monochrome, Cyber, Snow White
- **3D tilt cards** — cards rotate with mouse movement via perspective transforms
- **Particle network canvas** — 80 animated nodes with connection lines simulating client-server data flow
- **Smooth scroll reveal** — elements fade and slide up as you scroll
- **Floating gradient hero** — conic gradient animation + glow effects
- **Responsive** — works on desktop, tablet, and mobile

### 🎮 Interactivity
- **Tabbed content panels** — each question has 3-4 sub-tabs (Architecture, Analogy, Comparison Table, Summary)
- **Live theme demo** — toggle dark/light mode with real cookie readout
- **Keyboard navigation** — `←` `→` arrows and `Space` to move between sections
- **Auto-presentation mode** — click "Present" for auto-advancing slideshow (8s per section)
- **Fullscreen mode** — click the fullscreen button in the nav bar
- **Section counter & progress bar** — shows current position and reading progress
- **Interactive architecture diagram** — visual client↔server flow with animated arrows

### 🏗️ Architecture Visualizations
- **Client-Server architecture diagram** — HTTP request/response flow between browser and server
- **Comparison tables** — side-by-side Cookie vs Session across 9 dimensions
- **10-step stepper** — animated flow for Remember Me implementation
- **Device logout workflow** — visual explanation of selective session termination
- **Storage comparison matrix** — Cookie, Session, localStorage, sessionStorage evaluated across 6 criteria

### 🔒 Content Coverage
- **Cookie security flags**: Secure, HttpOnly, SameSite (Lax/Strict)
- **Facebook's TAO + Memcache** — eventual consistency for 3B+ users
- **Google's Spanner + TrueTime** — strong consistency for 1B+ users
- **SHA-256 token hashing** and database storage
- **Token rotation** — the single most important Remember Me security practice
- **Server-side vs client-only invalidation** for device logout
- **Security best practices** and common mistakes for each approach

---

## 🚀 Live Demo

**👉 [https://pavelgoblin.github.io/presentation/](https://pavelgoblin.github.io/presentation/)**

Click the link above to view the full interactive presentation in your browser. No installation required.

---

## 📂 File Structure

```
presentation/
├── index.html                   # Root redirect → web engineering/
├── web engineering/
│   ├── index.html               # Complete interactive presentation (single file)
│   └── README.md                # This file
└── .gitignore
```

**Everything is in a single HTML file** — no external CSS, JS, or library dependencies (except Google Fonts CDN for Inter font). Works offline after first load.

---

## 🖥️ How to Use

### Option 1: View Online (Recommended)
Visit **https://pavelgoblin.github.io/presentation/** in any modern browser (Chrome, Firefox, Edge, Safari).

### Option 2: Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/PavelGoblin/presentation.git
   ```
2. Open `index.html` in your browser:
   ```bash
   cd presentation
   start index.html     # Windows
   open index.html      # macOS
   xdg-open index.html  # Linux
   ```

### Navigation Tips
| Action | Control |
|--------|---------|
| Scroll through sections | Mouse wheel / touch scroll |
| Go to next section | `→` Arrow key or `Space` |
| Go to previous section | `←` Arrow key |
| Jump to question | Click Q1–Q5 in the nav bar |
| Switch tabs | Click tab buttons within each question |
| Toggle fullscreen | Click `⛾` button in nav bar |
| Start auto-presentation | Click `▶ Present` button |
| Change color theme | Click `🎨` palette button → choose swatch |

---

## 🎨 Color Themes

| Theme | Preview | Accent Colors |
|-------|---------|---------------|
| **Barca** (default) | 🟦🟥 | Blue + Red + Gold |
| **Midnight** | 🟣🟩 | Purple + Teal |
| **Forest** | 🟢🟠 | Green + Amber |
| **Sunset** | 🔴🟠 | Red + Orange |
| **Ocean** | 🔵🔵 | Cyan + Sky Blue |
| **Rose** | 🩷🟣 | Pink + Violet |
| **Monochrome** | ⚫⚪ | Grayscale |
| **Cyber** | 💚❤️ | Neon Green + Cyan |
| **Snow White** | ⚪🔵 | Light mode with blue accents |

Themes are saved in a persistent cookie — your preference survives browser restarts.

---

## 🛠️ Technical Details

### Built With
- **HTML5** — semantic structure
- **CSS3** — CSS custom properties (variables), glassmorphism, 3D transforms, flexbox/grid, keyframe animations, backdrop-filter
- **Vanilla JavaScript** — no frameworks, no libraries
- **Canvas API** — particle network animation
- **Fullscreen API** — native browser fullscreen
- **Intersection Observer API** — scroll-based reveal animations
- **Cookies** — theme preference persistence (color theme + dark/light mode)

### Browser Support
| Chrome | Firefox | Safari | Edge | Opera |
|--------|---------|--------|------|-------|
| ✅ 90+ | ✅ 90+ | ✅ 15+ | ✅ 90+ | ✅ 80+ |

### Performance
- **Single file** — ~57KB total (no network requests after font load)
- **Google Fonts** — only external dependency (Inter font, ~15KB cached)
- **Zero runtime dependencies** — no jQuery, no Bootstrap, no React
- **Offline-capable** — works after initial page load without internet

---

## 📚 Key Concepts Explained


### Cookie vs Session: The Fundamental Difference
```
┌─────────────────────────────────────────────────────────────┐
│                      HTTP is STATELESS                       │
│   Every request is independent — servers don't remember     │
│   who you are between requests without cookies/sessions.    │
└─────────────────────────────────────────────────────────────┘
```

| Aspect | Cookie | Session |
|--------|--------|---------|
| **Storage** | Client (browser) | Server (memory/Redis/DB) |
| **Size limit** | ~4KB per cookie | Virtually unlimited |
| **Visibility** | Visible to user + JavaScript | Hidden (only Session ID) |
| **Security** | XSS & CSRF vulnerable | More secure |
| **Lifetime** | Expires / Max-Age attribute | Server timeout (configurable) |
| **User control** | Can block or delete | Cannot block |
| **Performance** | No server resources | Uses server memory |
| **Analogy** | Library membership card | Bank locker (key + vault) |

### "Remember Me" — The 10-Step Flow
1. User logs in with credentials + checks "Remember Me"
2. Server validates credentials against hashed password
3. Server generates a cryptographically random 256-bit token
4. SHA-256 hash of token stored in database (never the raw token!)
5. Original token sent as persistent cookie (30-day Max-Age)
6. Cookie survives browser close (unlike session cookies)
7. Next visit: browser automatically sends the cookie
8. Server hashes received token and looks up in DB
9. If valid → auto-login user by creating new session
10. **TOKEN ROTATION** — delete old token, generate new, hash it, set new cookie

> ⚠️ **Critical:** Token rotation limits damage if a persistent token is ever stolen — it works only until the real user visits the site.

### Facebook vs Google: Consistency Trade-offs

| | Facebook (TAO) | Google (Spanner) |
|---|---|---|
| **Consistency model** | Eventual | Strong (ACID) |
| **Speed** | Very fast writes | Slightly slower writes |
| **Global sync** | May lag ~seconds | Always consistent |
| **Scale** | 3+ billion users | 1+ billion users |
| **Optimized for** | Social feed, messaging | Email, cloud storage, payments |

---

## 👨‍🏫 Instructor

**Mir Md. Kawsur**  
*Lecturer, Faculty — Department of Computer Science*  
*Adjunct Faculty, School of Science & Technology, BOU*

Passionate about coding, teaching, and spreading tech knowledge. Mir Md Kawsur, born in Dhaka, Bangladesh, completed his bachelor's and master's in computer science at American International University-Bangladesh (AIUB). With an unwavering love for coding, he embarked on a career as a programmer before transitioning to the fulfilling world of teaching.

---

## 📄 License

This project is for educational purposes as part of the Web Engineering course assignment.

---

## 🙏 Acknowledgments

- **Mir Md. Kawsur** — Course instructor for guidance and instruction
- **American International University-Bangladesh (AIUB)** — Academic foundation
- **School of Science & Technology, Bangladesh Open University (BOU)** — Academic affiliation

---

<p align="center">
  <strong>🍪 Cookies & Sessions — Web Engineering</strong><br>
  Mohammad Ibrahim | June 2026
</p>
