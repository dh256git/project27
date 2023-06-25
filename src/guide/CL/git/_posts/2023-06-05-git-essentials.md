---
layout: post
title: Add, commit, push - the git essentials
volume: digital skills
chapter: git
tag: git
---

There are only 3 Git commands you need to know, before you can start enjoying the benefits of Git.
Add, commit, and push.
<!-- excerpt-end -->

### Cheatsheet

To add, commit, and push changes in your current working directory, use the following git commands:

```
git add .
git commit -m '<your commit message>'
git push origin <name of remote branch>
```

### Before you start

For the following tip to work, we assume you have

- installed git in your command-line interface;
- Created a remote repository on GitHub, initialising it with a README file;
- cloned the remote repository to a local folder on your computer using the address GitHub provided;

Don't worry, we can write short notes on all of the above on demand.
In the meantime, we encourage you to ask Google, and to [get support]({% link support/index.md %}) from us.

### The 3 most used commands

To get started, open the README file in the repository, and change the text, then save the file.
Now switch to your command-line interface, and type the following commands.

```
git add .
git commit -m '<your commit message>'
git push origin <name of remote branch>
```

Let's unpick what all of this means.

#### Adding changes to the staging area

Every-time you modify a file, Git knows about it.
If you want your changes to be committed to version control, the first thing you need to do is adding the file to the so called staging area.
The way to do this is by writing the command:

`git add <file-name> <other-file-name>`

Note that you can add a single file, or multiple modified files.
However, you should avoid having spaces in your file name, as spaces separate commands and the name of files you want to add.

You can also add all the modified files in the current directory, by the following command:

`git add .`

The (.) character denotes "this directory". You can learn more about these shortcuts in our "BASH" chapter.

#### Committing changes

Great, now your modified files are staged.
Next, you need to commit them.
Use this command:

`git commit -m 'A commit message.'`

You can enclose a short message about the changes you made to help other people working on the project.
Keep it short though.
In following notes of this chapter, we will talk about good commit messages.

#### Pushing changes

Your changes are safe on your local machine.
However, if you want other people to see these changes, you will need to push your commits to the remote server.
This is how:

`git push origin master`

Here, `git push` is the basic command.
Once you link your local branch with a remote branch, the basic command is enough to get the job done.
To link branches between local and remote repositories, use the command:

`git push -u origin master`

Here, `origin` is the default name given to the remote repository.
It is a memorable word hiding the internet address of where your project lives.
The word `master` or `main` are the default branch names when you have a single branch working.
Names of remote repositories and branches can be changed.
If you want to push changes from another local branch to a remote branch, generally speaking you can use the command:

`git push <name-of-remote-repository> <name-of-remote-branch>`

### Next up

Well done if you were able to make your first commit.
To unlock the magic in the Git toolbox, there are a few more things to learn.
Quite a bit actually, but let's take it step by step.
In coming notes, we will introduce branching, and a typical development workflow.

Some commands to get excited about are:

- status, branch, checkout: welcome to the multiverse of Git.
- pull, merge, push: Avoiding conflict through best practice.