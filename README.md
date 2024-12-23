<div id="readme-top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />

## 🛒 LazyGrocer

###  By: Michael Montanaro, Colby Hegarty, Sanay Doshi
- Created for: CS3200 Database Design Final Project
- [![Github Actions][ghactionsLogo]][ghactionsLogo-url]

<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#structure">Structure</a></li>
    <li><a href="#tasks">Tasks</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Automatically generate your shopping list for a selected number of recipes. Import or manually add recipes to a locally stored database.

### Built With
[![Python][pythonLogo]][pythonLogo-url]
[![Docker][dockerLogo]][dockerLogo-url]
[![MySQL][mysqlLogo]][mysqlLogo-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Clone and navigate into the repository:
```bash
git clone git@github.com:montymi/LazyGrocer && cd LazyGrocer
```

On Unix Systems:
```bash
chmod +x ./start.sh
./start.sh -i
```
On Windows:
```bash
./start.sh
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Once the application is started in interactive mode, a container will startup, connect to the local mysql volume and prompt you with ID navigation through this menu:
```
Select Service:
1. Create
2. Read
3. Update
4. Delete
5. Quit
Service ID: _
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- STRUCTURE -->
## Structure
```
LazyGrocer/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── scripts/
│   └── init.sql
├── src/
│   ├── controller/
│   │   ├── dataControllerv2.py
│   │   └── __init__.py
│   ├── model/
│   │   ├── enums/
│   │   │   ├── scripts.py
│   │   │   ├── tables.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── testing/
│   │   ├── test_data_inserts.py
│   │   ├── test_data_selects.py
│   │   └── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   └── __init__.py
├── docker-compose.yml
├── Dockerfile
├── start.sh
├── README.md
└── LICENSE.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TASKS -->
## Tasks
- [ ] add exporting recipes as JSON
- [X] add installation instructions
- [X] add Structure section
- [ ] add Sanay and Colby information in Contact section
- [X] containerize for reproducibility
- [ ] add passive start in detached mode
- [ ] add APIs with FastAPI
- [ ] add CLI support when started in detached mode

See the [open issues](https://github.com/montymi/LazyGrocer/issues) for a full list of issues and proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

1. [Fork the Project](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. [Open a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Michael Montanaro - [LinkedIn](https://www.linkedin.com/in/michael-montanaro/) - montanaro.m@northeastern.edu

Project Link: [https://github.com/montymi/LazyGrocer](https://github.com/montymi/LazyGrocer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[ghactionsLogo]: https://github.com/montymi/LazyGrocer/actions/workflows/python-app.yml/badge.svg
[ghactionsLogo-url]: https://github.com/montymi/LazyGrocer/actions/workflows/python-app.yml
[pythonLogo]: https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=natural
[pythonLogo-url]: https://python.org/
[mysqlLogo]: https://img.shields.io/badge/MySQL-black?style=for-the-badge&logo=mysql
[mysqlLogo-url]: https://www.mysql.com/
[dockerLogo]: https://img.shields.io/badge/Docker-black?style=for-the-badge&logo=docker
[dockerLogo-url]: https://www.docker.com/
[contributors-shield]: https://img.shields.io/github/contributors/montymi/LazyGrocer.svg?style=for-the-badge
[contributors-url]: https://github.com/montymi/LazyGrocer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/montymi/LazyGrocer.svg?style=for-the-badge
[forks-url]: https://github.com/montymi/LazyGrocer/network/members
[stars-shield]: https://img.shields.io/github/stars/montymi/LazyGrocer.svg?style=for-the-badge
[stars-url]: https://github.com/montymi/LazyGrocer/stargazers
[issues-shield]: https://img.shields.io/github/issues/montymi/LazyGrocer.svg?style=for-the-badge
[issues-url]: https://github.com/montymi/LazyGrocer/issues
[license-shield]: https://img.shields.io/github/license/montymi/LazyGrocer.svg?style=for-the-badge
[license-url]: https://github.com/montymi/LazyGrocer/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-montanaro
