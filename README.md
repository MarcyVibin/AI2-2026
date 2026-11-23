<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<h3 align="center">Artificial Intelligence 2 — 2026</h3>

<p align="center">
    Solutions to the assignments of the course Artificial Intelligence 2 (2026): constraint programming, logic-based diagnosis, answer set programming and PDDL planning.
    <br />
    <br />
    <a href="https://github.com/MarcyVibin/AI2-2026/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/MarcyVibin/AI2-2026/issues">Request Feature</a>
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#assignments">Assignments</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## About The Project

This repository holds the models, encodings and write-ups for the Artificial Intelligence 2 assignments. Each assignment has its own folder with the source files and a short report in Markdown.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Assignments

| Folder | Topic | Files |
| --- | --- | --- |
| [A1](A1) | Constraint programming: backtracking with forward checking, and the "Super 512 Queens" problem | [1a.mzn](A1/1a.mzn) (MiniZinc model), [1b.py](A1/1b.py) (genetic algorithm skeleton), [report.md](A1/report.md) |
| [A2](A2) | Model-based diagnosis of a circuit as SAT / MaxSAT, and a grid puzzle in answer set programming | [circuit.dimacs](A2/circuit.dimacs), [circuit-observation1.dimacs](A2/circuit-observation1.dimacs), [diagnosis1.wdimacs](A2/diagnosis1.wdimacs), [diagnosis2.wdimacs](A2/diagnosis2.wdimacs), [instance.asp](A2/instance.asp), [placementA.asp](A2/placementA.asp), [placementB.asp](A2/placementB.asp), write-ups [exercise2a.md](A2/exercise2a.md) and [exercise2b.md](A2/exercise2b.md) |
| [A3](A3) | Planning in PDDL for a household robot | [domain.pddl](A3/domain.pddl), [problem.pddl](A3/problem.pddl), [exercise3.md](A3/exercise3.md); the task is in [assignment_sheet.pdf](A3/assignment_sheet.pdf) |

The PDFs next to the write-ups in `A2` are the exported versions of the Markdown reports.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
* [![MiniZinc][MiniZinc-badge]][MiniZinc-url]
* [![Clingo][Clingo-badge]][Clingo-url]
* [PDDL](https://planning.wiki/) for the planning domain and problem

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Requirements

- [MiniZinc](https://www.minizinc.org/) to run `A1/1a.mzn`
- Python 3 for `A1/1b.py`
- [clingo](https://potassco.org/clingo/) to run the `.asp` files (the reports were produced with clingo 5.7.2)
- A SAT / MaxSAT solver that reads DIMACS and WDIMACS for the `A2` encodings
- A PDDL planner for `A3`

### Installation

```sh
git clone https://github.com/MarcyVibin/AI2-2026.git
cd AI2-2026
```

---

## Usage

Run each assignment from its own folder, for example:

```sh
minizinc A1/1a.mzn
clingo A2/instance.asp A2/placementA.asp
```

The reports explain the models and show the results we got. Start with [A1/report.md](A1/report.md), [A2/exercise2a.md](A2/exercise2a.md), [A2/exercise2b.md](A2/exercise2b.md) and [A3/exercise3.md](A3/exercise3.md).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the GNU General Public License v3.0 (GPL-3.0). See `LICENSE` for more information.

---

## Contact

Marc Steger - marc.steger06@gmail.com

Project Link: https://github.com/MarcyVibin/AI2-2026

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Badge Links -->

[Python.org]: https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[MiniZinc-badge]: https://img.shields.io/badge/MiniZinc-Constraint%20Modelling-blue?style=for-the-badge
[MiniZinc-url]: https://www.minizinc.org/

[Clingo-badge]: https://img.shields.io/badge/clingo-Answer%20Set%20Programming-green?style=for-the-badge
[Clingo-url]: https://potassco.org/clingo/

[contributors-shield]: https://img.shields.io/github/contributors/MarcyVibin/AI2-2026.svg?style=for-the-badge
[contributors-url]: https://github.com/MarcyVibin/AI2-2026/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/MarcyVibin/AI2-2026.svg?style=for-the-badge
[forks-url]: https://github.com/MarcyVibin/AI2-2026/network/members

[stars-shield]: https://img.shields.io/github/stars/MarcyVibin/AI2-2026.svg?style=for-the-badge
[stars-url]: https://github.com/MarcyVibin/AI2-2026/stargazers

[issues-shield]: https://img.shields.io/github/issues/MarcyVibin/AI2-2026.svg?style=for-the-badge
[issues-url]: https://github.com/MarcyVibin/AI2-2026/issues

[license-shield]: https://img.shields.io/github/license/MarcyVibin/AI2-2026.svg?style=for-the-badge
[license-url]: https://github.com/MarcyVibin/AI2-2026/blob/main/LICENSE
