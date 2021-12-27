<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/9/92/LaTeX_logo.svg" width="320px" />

# Template LaTeX Project

![Release Version](https://img.shields.io/github/v/release/mundoalem/template-latex-project)
![Workflow Status](https://github.com/mundoalem/template-latex-project/actions/workflows/on_tag.yml/badge.svg)
![Contributors](https://img.shields.io/github/issues/mundoalem/template-latex-project)

A DevOps centric template to bootstrap LaTeX projects.

</div>

## Introduction

This project is a template anyone can use in order to bootstrap a project using the LaTeX language. The template has a
full featured pipeline following the latest DevOps practices.

You can control the project through the use of [invoke](https://docs.pyinvoke.org/en/stable/), it accepts the following
targets:

| Argument | Description                                |
| -------- | ------------------------------------------ |
| build    | Build the document as a PDF file           |
| clean    | Remove build files and directories         |
| format   | Formats the files                          |
| lint     | Check the code for syntax issues and style |
| release  | Release the document                       |
## License

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Tech Stack

These are the software baked in this template:

- [TexLive 2021](https://www.tug.org/texlive/)
- [chktex](https://www.nongnu.org/chktex/)
- [latexindent](https://github.com/cmhughes/latexindent.pl)

## Usage

In order to use this template you first need to clone this repo locally:

```
$ git clone git@github.com:mundoalem/template-latex-project.git
$ cd template-latex-project/
```

After you finish cloning the template you can start using it right away, however
it may be better to make the project your own by:

- Update the `document.tex` file with your project details.
- Add your license to `LICENSE` file.
- Update the license header in all LaTeX files.
- Configure in `.chktex` the checks you want to make or ignore during the lint phase.
- Update the `README.md` with your project information.
- Update `settings` section in `.devcontainer/devcontainer.json` with your preferred Visual Studio Code settings.

All pipeline jobs can be also run locally by invoking `invoke` tasks, example:

```
$ invoke build
$ invoke format
$ invoke lint
```

The content of the document starts in the `document.tex`. That file will set the initial document information such the
title, date, authors, etc. Appendices, sections, figures and etc can be found in the `content` directory.

This template was designed for academic papers but can be easily modified for any kind of works.

## Environment Variables

To run this project, you will need to add the following environment variables to your environment:

| Variable | Description                                                                                    |
| -------- | ---------------------------------------------------------------------------------------------- |
| CI       | Variable used to determine whether the `invoke` tasks are bring run locally or in the pipeline |

## Feedback

If you have any feedback, please open an [issue](https://github.com/mundoalem/template-latex-project/issues).

## Contributing

In particular, this community seeks the following types of contributions:

- Participate in an issue thread or start your own.
- Help us ensure that this repository documentation is comprehensive.
- Implement new features to the project.
- Fix open issues.

## Conduct

We are committed to providing a friendly, safe and welcoming environment for all, regardless of gender, sexual
orientation, disability, ethnicity, religion, income or similar personal characteristic.

Please be kind and courteous. There's no need to be mean or rude. Respect that people have differences of opinion and
that every design or implementation choice carries a trade-off and numerous costs. There is seldom a right answer,
merely an optimal answer given a set of values and circumstances.

Please keep unstructured critique to a minimum. If you have solid ideas you want to experiment with, make a fork and see
how it works.

We will exclude you from interaction if you insult, demean or harass anyone. That is not welcome behavior. We interpret
the term "harassment" as including the definition in the [Citizen Code of Conduct](http://citizencodeofconduct.org/);
if you have any lack of clarity about what might be included in that concept, please read their definition. In
particular, we don't tolerate behavior that excludes people in socially marginalized groups.

Whether you're a regular contributor or a newcomer, we care about making this community a safe place for you and we've
got your back.

Likewise any spamming, trolling, flaming, baiting or other attention-stealing behavior is not welcome.

## Communication

GitHub issues are the primary way for communicating about specific proposed changes to this project.

In both contexts, please follow the conduct guidelines above. Language issues are often contentious and we'd like to
keep discussion brief, civil and focused on what we're actually doing, not wandering off into too much imaginary stuff.

## FAQ

### Will there ever be support for other continuous integration platforms?

Right now I have no plans to support other platforms like TravisCI, CircleCI or Gitlab. Anyway, it should be quite
easy for you to port the GitHub Actions to any platform you like.

The reason for that is that I don't want to have a `.travis.yml`, a `circleci.yml` and a `.gitlab-ci.yml` all together
in the same place when only one would actually be used. So I want to avoid (for now) cluttering the template with too
many files that might or might not be useful.

### I don't like Visual Studio Code! Are you going to support other text editors?

That's also a difficult topic since text editors and IDE's all work in different ways and support different features.
The reason for Visual Studio Code (vscode) is because it is free, open source, widely adopted by the community,
supports remote development and enables me to have all the editor configuration as code.

Other development environments might be better in some aspects, but there is little room to customize their workflow
and you can't share it in an easy way.

As a DevOps engineer you are always trying to improve agility by creating automation that facilitates other people's
workflows. Unfortunately, it's easy to face frustration and resistance as most people get used to their tools and their
own ways of doing things.

Having said that, you can still make use of the template for other text editors and IDE's but you will need to find out
on your own how to integrate the features of this template to those tools.