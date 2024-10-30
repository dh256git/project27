---
layout: post
title: "Status, Branch, Checkout: Welcome to the Multiverse of Git"
volume: digital skills
chapter: git
tag: git
image: /guide/git-multiverse.webp
alt: A time-travel scene with a developer holding a 'checkpoint pass,' stepping through a glowing portal with futuristic elements. The portal displays different branch names and commit hashes as destinations, symbolizing a journey through code versions. The developer appears focused, wearing casual tech attire, ready to step into the portal.
---

In the world of Git, we’re not just managing code; we’re managing entire timelines. Think of Git as a multiverse where each command opens a portal to a different version or a new line of code reality. If you’re new to Git or looking to solidify your understanding, today we’re diving into three essential commands that will help you navigate this multiverse: `status`, `branch`, and `checkout`.
<!-- excerpt-end -->

### **Cheatsheet: Essential Git Commands**

Use this cheatsheet as a quick reference to navigate Git’s multiverse with ease:

| **Command**                 | **Usage**                                                                                                      |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------|
| **`git status`**            | Shows the current state of your working directory and staging area. Use it to see modified, staged, or untracked files. |
| **`git branch`**            | Lists all branches in the repository, highlighting the active branch.                                          |
| **`git branch <branch-name>`** | Creates a new branch named `<branch-name>` from the current branch’s HEAD.                                        |
| **`git branch -d <branch-name>`** | Deletes the specified branch. This is useful for cleanup after merging changes.                             |
| **`git checkout <branch-name>`** | Switches to the specified branch, updating your working directory to reflect that branch’s files.            |
| **`git checkout -b <new-branch>`** | Creates a new branch and switches to it immediately, saving a step.                                       |
| **`git checkout <commit-hash>`** | Temporarily views the project state at a specific commit. Perfect for exploring or debugging past versions.  |

### **Before you start**

We assume you familiarised yourself with the git essentials.
If you haven't yet, check our post out on [Add, commit, push: The git essentials.]({% post_url 2023-06-06-git-essentials %})

### **Status: Checking the Pulse of Your Repository**

The `git status` command is your way of taking the pulse of your Git repository. It shows you what’s happening in your current branch, giving you a quick overview of what’s 'staged', what’s 'unstaged', and what’s 'untracked'.

Think of `git status` as the command that helps you get your bearings. When you type `git status`, Git will tell you where you stand:
- Are there changes not yet staged for commit?
- Are there untracked files that aren’t being watched by Git?
- Is your branch up-to-date with its remote counterpart?

#### **Common Uses of `git status`**
1. **Check for Modified Files** – Before committing, it’s always good practice to see what’s changed.
2. **Track Untracked Files** – New files created in your project won’t automatically be tracked; `git status` lets you see what needs to be added.
3. **Confirm Your Branch State** – Avoid surprises by ensuring your branch has no unexpected changes before pushing.

### **Branch: Creating New Realities**

A `branch` in Git is like a parallel universe for your code. It allows you to create an independent line of development, where you can experiment, add new features, or fix bugs without touching the main universe (or branch). In Git, creating a branch is as simple as a command.

```bash
git branch feature-xyz
```

With that command, you’ve created a new branch, `feature-xyz`, where you can build in isolation. Changes you make here won’t affect the main branch (often called `main` or `master`) until you merge them.

#### **Key `git branch` Commands**
1. **Creating a Branch**: `git branch <branch-name>` – Creates a new branch from the current HEAD.
2. **Listing Branches**: `git branch` – Shows all branches in your repo and highlights the one you’re currently on.
3. **Deleting a Branch**: `git branch -d <branch-name>` – Once you’re done with a branch, you can delete it to keep things tidy.

Branches allow you to manage multiple features or updates without interfering with other development work. They’re perfect for collaboration, too, as each developer can work on their branch without worrying about conflicts.

### **Checkout: Traveling Between Branches**

If branches are alternate realities, then `git checkout` is your time machine. This command allows you to switch between branches or revisit a specific commit, enabling you to jump between different versions of your project with ease.

To switch to an existing branch, you simply use:

```bash
git checkout feature-xyz
```

Now, you’re in the `feature-xyz` universe, working in an isolated environment. Need to return to the main branch? Just type `git checkout main`, and you’re back where you started.

#### **Common `git checkout` Scenarios**
1. **Switching Branches**: Move between branches to keep up with ongoing development.
2. **Creating a New Branch and Switching**: `git checkout -b <new-branch>` – Creates and checks out a new branch in one command.
3. **Checking Out a Specific Commit**: Use `git checkout <commit-hash>` to explore an earlier commit.

It’s essential to remember that using `checkout` will change your working directory to match the state of the branch or commit you’ve selected. Any unsaved changes can get lost, so always `commit` or `stash` your work if you’re jumping around.

### **The Power Trio of Git: Status, Branch, and Checkout**

With `status`, you’re always aware of where you are. With `branch`, you can explore new possibilities, and with `checkout`, you have the freedom to jump between those possibilities at will. Together, these commands form the backbone of your Git workflow, allowing you to keep your code organised, explore new ideas safely, and collaborate seamlessly.

By mastering `status`, `branch`, and `checkout`, you gain the ability to navigate Git’s multiverse with confidence, focusing on what really matters: creating, experimenting, and shipping code.

