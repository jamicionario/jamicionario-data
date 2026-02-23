
# Jamicionário data

This repository has the data used in the [Jamicionário](https://jamicionario.github.io).

**Contributions are welcome! ❤️**  
Fork, edit, and open a pull request to merge your changes back here.  
They will be published to the Jamicionário, with love.

In this document:

- [Issues](#issues)
  - [Bug reports](#bug-reports)
    - [Template](#template)
  - [Feature requests](#feature-requests)
- [Contributing](#contributing)
  - [As a member of Jamicionário](#as-a-member-of-jamicionário)
  - [As an external contributor](#as-an-external-contributor)
  - [Good commit messages](#good-commit-messages)
- [First-time setup](#first-time-setup)

We know it's a lot of text.  
Read it diagonally, and come back to it as you need. :)

## Issues

You can use the [Issues](https://github.com/jamicionario/jamicionario-data/issues) page to report issues with the data.

If they are **issues with the Jamicionário site**, please report them [in the Jamicionário's repository](https://github.com/jamicionario/jamicionario.github.io/issues) instead.

When submitting an issue:

- Fill in the _Labels_ and choose a _Type_.
- Be friendly.  
  This is a voluntary community, it runs on good vibes. :)
- Try to be clear.  
  Simple wording and explicit meanings, that helps a lot.

### Bug reports

If you find a bug, do report it!

A good bug report:

1. Has a title that describes the problem.
   - _Good: "Navigation broken on the score details page."_
   - Weak: "Can't open link."
2. Includes the steps to reproduce.
   - _Great: "Open details for a score, example /scores/30 . Press the arrow to the right."_
   - _Good: "I don't know how to reproduce. But it happened in the score details page, when I went there from the search."_
   - Bad: "Arrow does not work."
3. Includes what was expected to happen.
   - _"When I am in score 28 and click the arrow to the right, it should open score 29."_
4. Includes what happened instead.
   - _"Instead, it navigates to score 51?? And then from 51 it navigates to 51 as well."_

#### Template

Here's a good template for bug reports:

> (Title)
>
> (Description, if useful)
>
> Steps to reproduce:
>
> 1. […]
>
> Expected result: […]
>
> Actual result: […]

These fields are really important to provide.  
You can then include more information that you think can be helpful.

### Feature requests

When submitting a feature request, try to outline how you think it would improve the Jamicionário.

Include details you have thought about, and if you know of possible problems or difficulties that is also useful to include.

If you want to be extra helpful, also describe the feature from the point of view of a user!  
Example:  
> "As a musician, I would like the whole score to fit on the screen automatically, so that I don't need to zoom or scroll. It is very difficult for musicians to use their hands for handling the scores while playing."

## Contributing

If it is your first time here, first check the section [First-time setup](#first-time-setup) below.

Here is the process for contributing.  
It is a bit technical but not too difficult — it may feel unfamiliar and a bit arcane, but it is very repetitive and straightforward.  
We will help if needed.

So:

### As a member of Jamicionário

If you are a member of Jamicionário:

- Make a new branch.
- Do some changes, review and commit.
- Repeat with more work you want to share.
- Then make a Pull Request to `main`.

In detail:

Let's pretend that we are Michel,  
our github username is `m-giacometti`,  
and we want to add scores for [Béarnaise dances](https://fr.wikipedia.org/wiki/Danse_b%C3%A9arnaise) to the Jamicionário.  
We can do that work in a branch named `add-bearnaise-songs`, like so:

1. Checkout the branch "main" with `git checkout main` and do `git pull` to make sure it is up to date.
2. Create a new branch with `git checkout -b add-bearnaise-songs`.
3. You are ready and can make your editions to the files.
4. Review your editions to prepare a commit:
   1. View what has changed with `git status`
   2. Select new or changed files to be comitted with `git add "Saut Béarnais.mscz` , or do `git add .` to add all files in the current folder.  
      This is called "staging". These files are stages for commit, and will be included in the commit. Unstaged files will not be included in the commit.
   3. And make a commit with `git commit`.  
      If you are using a graphical git tool and commit with nothing staged, it will usually assume you want to commit all pending changes.
   4. You will be asked for a commit message, which you can also provide with `git commit -m "Added score for Saut Béarnais."`.
      1. It's important and useful to have a good commit message.
      2. Check the section [Good commit messages](#good-commit-messages) below.
5. If you have several changes to do, it's good form to put them in different commits.  
   This is easier to understand and work with, than a very big changeset.
6. When you are done, push your branch with `git push origin`.
7. Go to the [Pull Requests](https://github.com/jamicionario/jamicionario-data/pulls) page and create a new pull request, from your branch `add-bearnaise-songs` to the branch `main`.
   1. Follow the instructions.
   2. You will see the changes included, etc. The UI guides you through it.
   3. Remember to be descriptive in what changes you are sharing.  
    Especially with binary files such as the MuseScore .mscz files, it is difficult to know what changes were done.

### As an external contributor

If you are an external contributor, the process is similar, but:

1. First you "[fork ℹ️](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)" the repository to your own account.
   1. Look for the _[Fork]_ button on the root page of the repository, which opens this page:  
      https://github.com/jamicionario/jamicionario-data/fork
   2. After you forked the repository, you have an independent copy of it in your personal page:  
      https://github.com/m-giacometti/jamicionario-data  
      It is related to the Jamicionário repository, but independent.
2. Then you follow all the same steps as explained above, 1–6, but on your repository (m-giacometti/jamicionario-data).
3. And in step 7. the end, when creating the Pull Request, you will target this repository instead of your own.
   1. So, where a member of Jamicionário makes a Pull Request from `add-bearnaise-songs` to `main`;
   2. You will do a Pull Request from `m-giacometti/add-bearnaise-songs` to `jamicionario-data/add-bearnaise-songs` .
4. The rest is the same; except we love you extra. :)

### Good commit messages

#### Why?

Each commit is a piece of our work.  
The way we organize them can really help: understanding what is happening, and feeling confortable and confident in what we are doing.

Try reading the commits for this repository:  
https://github.com/jamicionario/jamicionario-data/commits/main/

Some will be clear to you and some will not.  
Ideally they would all feel informative and clear.

As they accumulate over time, they may be hundreds, like in the Jamicionário repository:  
https://github.com/jamicionario/jamicionario.github.io/commits/main/

#### How?

- Small commits are better, grouping a small set of changes together.
- Writing a good commit message is important. The message should be short, clear, and identify the changes done.
- If you want to include more information, have a first sentence as a title, leave a line of space, and then write what you feel is useful. :)  
  - See for example the commit "[Fix 0-width voltas for all files.](https://github.com/jamicionario/jamicionario-data/commit/b62ebbf6b1608b7c77efea7445891d33a5f7b9e4)".
  - The title is short and says clearly what was done... _if_ you understand the context, and have looked at it before.
  - But if not, it has a long descripton explaining what the difficult problem was, and how it was resolved.
    - This is a more technical commit, this type of commits will be rare. But because the problem was difficult to address, we opted to document it well.

Good examples, clear and concise:

- "Updated the 'regions' for all the Walz scores."
- "Added Xota da Guia and Xota de Bembibre."
- "Changed the organization of Sbrando's parts to match the traditional dance." — a bit wordy, but still good; it could probably be improved with a description.

Bad examples:

- "Fixes issues with some scores." — Which issues? Are they important? Do they maybe affect other scores? Are they well resolved?
- "added more" — Difficult to know what was done.
- "Fix Regadinho" — How? What was wrong, or what became better? Could it maybe even be a problem affecting other files?

## First-time setup

If you are new to git, you may want to consider using a graphic client like [GitHub Desktop](https://github.com/apps/desktop).  
The instructions here will be for using the terminal, but a graphical interface helps a lot.

You will need to:

1. Decide if you will use a graphical client or the terminal/command line.
   A graphical client will install git for you.  
   Otherwise, you might want to use [git-scm](https://git-scm.com/install). They have detailed instructions for all operating systems.
2. After you install git, first configure your identity:
   1. `git config --global user.name "Michel Giacometti"`
   1. `git config --global user.email "m-giacometti@example.org"`
3. If you will use git via SSH, you need to set it up in the [SSH keys settings](https://github.com/settings/keys) of your GitHub profile. That page has a link to a guide.
4. Then clone the repository:
   1. Navigate to the folder where you will want it, such as "/users/m-giacometti/code";
   2. And clone the repository:  
      either via SSH: `git clone git@github.com:jamicionario/jamicionario-data.git`  
      or via HTTPS: `git clone https://github.com/jamicionario/jamicionario-data.git`
5. If you want to contribute and send changes back, you will need to have a github account. [Create one](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) if needed.

You should now have a folder "jamicionario-data" with the contents of this repository.  
Go back and continue reading the section [Contributing](#contributing) from the start.
