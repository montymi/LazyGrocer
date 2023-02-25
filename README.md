<div id="readme-top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Reviving OSS Documentation</h2>

  <p align="center">
    Created by: Michael Montanaro
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/montymi/ClearDocs">View Demo</a>
    ·
    <a href="https://github.com/montymi/ClearDocs/issues">Report Bug</a>
    ·
    <a href="https://github.com/montymi/ClearDocs/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
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
## Problem Statement

Open-source software has a high barrier of entry due to source code disorganization, caused mainly by a lack of structured documentation. For this project, I will create a brief GitHub README file to depict an ideal version of the file and argue that the current state of OSS's documentation is not acceptable. OSS documentation must find a method of tracking and portraying project information that is universally accepted within the open-source community. 

## About The Project

The Open Source Software (OSS) community is the backbone of countless businesses around the world, with more than 50% of Fortune 500 companies relying on it for their workflow. That number is set to grow as more open source projects advance and gain traction in the work force, but this will only happen with consistent feature implementation. Increased demand in new features is difficult to match without a subsequent increase in developers. In a study done by Ravi Sen, Siddhartha S. Singh, and Sharad Borle, it was found that "an increase in the number of developers by 10 leads to a 5.65% increase in the average number of subscribers." As evidenced by this statistic, there is a direct correlation between the number of workers on a project and the number of users/subscribers to the service that is being created. 

This would lead one to believe that the OSS community should be doing everything in its power to lower the projects barrier of entry and welcome edits and suggestions from the community, which is the main goal of OSS. However, not only is this not currently a priority, but also, structural documentation is usually still omitted altogether, with only 5.4% of 2000 projects investigated in a 2014 study having any sort of architectural documentation. Many open source projects have already grown by enormous proportions, but it is not difficult to say that if a higher percentage of projets were to put an emphasis on software architecture documentation, the community and countless other lesser-known projects would thrive. 

Documentation must serve to guide a user or possible developer through the project's intended use case as well as the current workflow and future plans. It isn't enough to simply have a brief explanation of the project and an installation guide with a few use case examples. Outside developers must be able to quickly navigate the source code and pick up on the tasks that are waiting to be completed. Users should have a sense of the future plans for the project as well as a clear means of communicating with the current developers. 

This README hopes to serve as a template for what documentation should look like in order to greatly improve the approachability of OSS projects and encourage more contributions from the community and any newcomer trying to grow as a programmer. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

By listing the major libraries used in the project, the project will show up in filtered search results for any library listed. The list also allows a developer to quickly see if a library in which they are well-versed is a part of the project. Check the "Mardown Links and Images" section of the HTML version of this file to see how these logo-url's are created.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

*Here is an example of installation instructions by one of the largest Python projects on GitHub: [cpython](https://github.com/python/cpython). This section should walk through installation on various operating systems as well as any installation options. The readability of this section will make or break whether someone will use the project, since this section is often the most looked at section (only behind the [About the Project](#about-the-project) section).*

On Unix, Linux, BSD, macOS, and Cygwin:

```
./configure
make
make test
sudo make install
```
This will install Python as python3.

You can pass many options to the configure script; run ./configure --help to find out more. On macOS case-insensitive file systems and on Cygwin, the executable is called python.exe; elsewhere it's just python.

Building a complete Python installation requires the use of various additional third-party libraries, depending on your build platform and configure options. Not all standard library modules are buildable or useable on all platforms. Refer to the Install dependencies section of the Developer Guide for current detailed information on dependencies for various Linux distributions and macOS.

On macOS, there are additional configure and build options related to macOS framework and universal builds. Refer to Mac/README.rst.

On Windows, see PCbuild/readme.txt.

If you wish, you can create a subdirectory and invoke configure from there. For example:

```
mkdir debug
cd debug
../configure --with-pydebug
make
make test
```
(This will fail if you also built at the top-level directory. You should do a make clean at the top-level first.)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Users are much more likely to use and test a project if they can quickly determine how best to use the software and whether or not it really is what they are looking for. Clear usage examples also give incoming developers a chance to better understand the code and its intended use.

*Here is an example from a project for getting the weather via CLI by [genuinetools](https://github.com/genuinetools)*

```
# get the current weather in your current location
$ weather

# change the units to metric
$ weather -l "Paris, France" -u si

# it will auto guess the units though so changing
# the location to paris will change the units to `si`
$ weather -l "Paris, France"

# get three days forecast for NY
$ weather -l 10028 -d 3

# or you can autolocate and get three days forecast
$ weather -d 3

# get the weather in Manhattan Beach, CA
# even includes alerts
$ weather -l "Manhattan Beach, CA"
#                             .;odc
#                           ;kXNNNO
#                         .0NNO0NN:
#                        'XNK; dNNl
#                        KNX'  'XNK.
#                       ,NNk    cXNK,
#                       ,NNk     '0NNO:.
#                     .'cXNXl;,.   ,xXNNKOxxxk0Xx
#                 'lOXNNNNNNNNNNXOo'  ':oxkOXNNXc
#               cKNNKd:'.    ..;d0NNKl    ,xXNK,
#        .;:cclKNXd.              .oXNXxOXNNXl
#    .cOXNNNNNNNO.                  .kNNNNNNNXOc.
#   lXNXx;.    .                      .    .;dXNXo
#  ONNd.                                       oXN0.
# dNNo                                          cNNk
# XNN.                                           NNX
# 0NN'                                          .NNK
# ;XN0.                                        .ONNc
#  ;XNXo.                                    .lXNX:
#   .oXNX0dlcclx0Xo.              .oXKxlccldOXNXd.
#      ,lk0KXXK0xKNN0o;..    ..;o0NNKx0KXXX0ko,
#                 'lOXNNNNNNNNNNXOo,
#                     :x0XNNX0x:.
#
#
# Current weather is Partly Cloudy in Manhattan Beach in California for July 14 at 4:14am EDT
# The temperature is 69.2°F, but it feels like 69.2°F
#
# Special Weather Statement for Los Angeles, CA
# ...THREAT OF MONSOONAL THUNDERSTORMS LATE TONIGHT THROUGH WEDNESDAY...
# A STRONG UPPER LEVEL HIGH PRESSURE SYSTEM CURRENTLY CENTERED OVER NEVADA
# WILL BRING INCREASING EAST TO SOUTHEAST FLOW OVER SOUTHERN
# CALIFORNIA. AS A RESULT...A SIGNIFICANT SURGE OF MONSOONAL MOISTURE
# WILL MOVE INTO SOUTHWEST CALIFORNIA LATE TONIGHT THROUGH WEDNESDAY.
# THE GREATEST THREAT OF SHOWERS AND THUNDERSTORMS WILL BE ACROSS THE
# MOUNTAINS AND ANTELOPE VALLEY LATE TONIGHT INTO TUESDAY. DUE TO THE
# EASTERLY UPPER LEVEL FLOW ON MONDAY...THERE WILL ALSO BE A SLIGHT
# CHANCE OF SHOWERS AND THUNDERSTORMS ACROSS MOST COASTAL AND VALLEY
# AREAS.
# THE DEEPER MONSOONAL MOISTURE WILL BRING THE POTENTIAL FOR BRIEF HEAVY
# RAINFALL WITH STORMS THAT DEVELOP ON MONDAY AND TUESDAY...ESPECIALLY
# ACROSS THE MOUNTAINS AND ANTELOPE VALLEY. WHILE STORMS ARE EXPECTED
# TO BE FAST MOVING...THERE WILL BE THE POTENTIAL FOR LOCALIZED FLOODING
# OF ROADWAYS AND ARROYOS. ON TUESDAY...THE THREAT OF THUNDERSTORMS IS
# EXPECTED TO REMAIN CONFINED TO THE MOUNTAINS AND DESERTS. WITH WEAKER
# UPPER LEVEL WINDS ON TUESDAY...STORMS WILL LIKELY MOVE SLOWER. AS A
# RESULT...THERE WILL BE AN INCREASED THREAT OF FLASH FLOODING.
# IT WILL NOT BE AS HOT ACROSS MUCH OF THE REGION TOMORROW DUE TO THE
# INCREASED MOISTURE AND CLOUD COVERAGE...WITH INTERIOR SECTIONS
# GENERALLY REMAINING IN THE 90S. HOWEVER...THERE WILL BE A
# SIGNIFICANT INCREASE IN HUMIDITY ON MONDAY THAT WILL CONTINUE TO
# BRING DISCOMFORT.
# ANYONE PLANNING OUTDOOR ACTIVITIES IN THE MOUNTAINS AND DESERTS
# DURING THE NEXT FEW DAYS SHOULD CAREFULLY MONITOR THE LATEST
# NATIONAL WEATHER SERVICE FORECASTS AND STATEMENTS DUE TO THE
# POTENTIAL HAZARDS ASSOCIATED WITH THUNDERSTORMS.
#             Created: July 13 at 10:50pm EDT
#             Expires: July 14 at 7:00pm EDT
#
# Ick! The humidity is 85%
# The nearest storm is 18 miles NE away
# The wind speed is 3.96 mph SE
# The cloud coverage is 35%
# The visibility is 9.58 miles
# The pressure is 1012.99 mbar
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- STRUCTURE -->
## Structure

As stated above, less than 6% of GitHub projects include documentation or diagrams about the software's architecture. Since larger projects can often have a very convoluted source code structure, diagrams are the ideal method of displaying the flow of the project. 

*Here is an example given by the official [PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML) GitHub page which utilizes both graphical and verbal descriptions to portray the workflow of a web application.*
<div align="center"><img width="830" alt="Example software architecture drawn via PlantUML" src="https://user-images.githubusercontent.com/84359773/201444996-30331b8e-69c2-4440-bf0b-a79610282772.png"></div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TASKS -->
## Tasks

By publicly displaying the to-do list of the project, users are able to see any feature that is nearing implementation. The list also allows new developers to quickly find potential tasks for them to complete which is an ideal way to familiarize them with the source code and to continue to make commits.

- [X] Emphasize 5.4% of projects section (speculation about what the observable differences would be if it were a higher figure)
- [X] Fix "Built With" logos section
- [X] Revision at the sentence level
- [X] Center architecture image
- [X] Add Author's Note
- [X] Fix some links
- [ ] Add beginner project to repository
- [ ] Change code examples to be example project

See the [open issues](https://github.com/montymi/ClearDocs/issues) for a full list of issues and proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are, in my opinion, the greatest part of OSS and are what will be the key to continuing the growth of the community. One of the main goals of this README is to facilitate contributions of potential developers. In this section, developers must be sure to lay out any coding styling choices that they may have so that the source code can remain as uniform as possible. One such project that has an immpressive contributions page is *htop* by [htop-dev](https://github.com/htop-dev/htop) who point all potential incoming contributors to their [style guide](https://github.com/htop-dev/htop/blob/main/docs/styleguide.md)

1. [Fork the Project](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. [Open a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

*Documentation must include a license section in which the type of license and a link or reference to the full license in the repository is given.*

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Michael Montanaro - [LinkedIn](https://www.linkedin.com/in/michael-montanaro/) - montanaro.m@northeastern.edu

Project Link: [https://github.com/montymi/ClearDocs](https://github.com/montymi/ClearDocs)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list any resources used or that may be helpful in understanding the project

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/montymi/ClearDocs.svg?style=for-the-badge
[contributors-url]: https://github.com/montymi/ClearDocs/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/montymi/ClearDocs.svg?style=for-the-badge
[forks-url]: https://github.com/montymi/ClearDocs/network/members
[stars-shield]: https://img.shields.io/github/stars/montymi/ClearDocs.svg?style=for-the-badge
[stars-url]: https://github.com/montymi/ClearDocs/stargazers
[issues-shield]: https://img.shields.io/github/issues/montymi/ClearDocs.svg?style=for-the-badge
[issues-url]: https://github.com/montymi/ClearDocs/issues
[license-shield]: https://img.shields.io/github/license/montymi/ClearDocs.svg?style=for-the-badge
[license-url]: https://github.com/montymi/ClearDocs/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-montanaro
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
