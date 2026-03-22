# 🚀 NyayaSahayak Project – Development Workflow Guide

## 🧠 Overview

This project follows a structured Git workflow to ensure:


## 🌿 Branch Structure

### 🔹 `main` (Sacred Branch)

* This is the **final, stable version** of the project
* 🚫 No direct commits allowed
* Only updated through PR from `Integration`

---

### 🔹 `Integration` (Working Branch)

* All team code is merged here first
* Acts as the **testing and integration layer**
* 🚫 No direct commits allowed (use PR only)

---

## 🔄 Development Workflow

Follow these steps for every task:

---

### 🟢 Step 1: Create a Feature Branch

Always create a new branch from `Integration`:

```bash
git checkout Integration
git pull origin Integration
git checkout -b feature/<feature-name>
```

Example:

```bash
git checkout -b feature/login-system
```

---

### 🟡 Step 2: Work on Your Feature

* Write clean, readable code
* Test your changes locally

---

### 🔵 Step 3: Commit Your Code

```bash
git add .
git commit -m "Add login system"
```

---

### 🟣 Step 4: Push Your Branch

```bash
git push origin feature/<feature-name>
```

---

### 🔴 Step 5: Create Pull Request (PR)

On GitHub:

* Base branch: `Integration`
* Compare branch: your feature branch

Add:

* Clear title
* Description of changes


## 🔀 Merging Rules

* Feature branches → merged into `Integration`
* After testing, `Integration` → merged into `main`

---


## ⚠️ Important Rules

* ❌ Do NOT push directly to `main`
* ❌ Do NOT push directly to `Integration`
* ✅ Always use Pull Requests
* ✅ Keep branch names meaningful

---

## 🏷️ Branch Naming Convention

Use clear and structured names:

```
feature/<feature-name>
bugfix/<issue-name>
```

Examples:

* `feature/login`
* `feature/api-endpoint`
* `bugfix/auth-error`
