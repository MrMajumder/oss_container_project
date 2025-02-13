<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
<!-- [![Youtube Link][youtube-shield]](https://youtu.be/LVSId1obOoE) -->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/MrMajumder/oss_container_project">
    <img src="images/weakness.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">INSE 6130: Operating Systems Security Project</h3>
  <p align="center">
    A project on exploiting containers, as well as preventing the exploit.
    <br />
    <br />
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
        <li><a href="#project-images">Project Images</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributors">Contributors</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

**Motivation**: Container escape is a term describing a type of vulnerability in which an attacker successfully gains unauthorized access to the host system's resources and data from within the container, either through executing a malicious image or building an image using a malicious Dockerfile or upstream image. Once an attacker gains access to the underlying host operating system, they could potentially access whatever data was on the system, including sensitive data (credentials, customer info, etc.), and launch further attacks.

In this project, we explore five (5) vulnerabilities related to container escape (including one recent 2024 CVE). We are divided into two teams: attacker and defenders. The attackers implemented the exploits for the 5 vulnerabilities, where the defenders created an ELK stack based log monitoring solution, where the system calls were correlated to detect the exploits.

This project was developed for the "INSE 6130: Operating Systems Security", Winter 2024 course. Find the [slides](./presentation.pptx) and [final report](./report.pdf) here.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With
Python, Shell Scripting, Elastic Search, Kibana, Logstash


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how to set up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MrMajumder/oss_container_project
   ```
2. The `Attack` folder contains the implementation of the attacks.
3. The `ELK Codes` contains the code to run the ELK stack. and `ELK Stack` contains the shell scripts to spin on, off the ELK stack, its installation etc.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributors

* Shafayat Hossain Majumder - [GitHub][github-url] | [LinkedIn][linkedin-url] | [Mail][email] | [Website][website-url]
* Piyush Adhikari - [GitHub][https://github.com/adhikari-piyush41] | [LinkedIn][https://www.linkedin.com/in/piyush-adhikari/] | [Mail][mailto:adhikaripiyush41@gmail.com]
* Sourov Jajodia
* Tariq Houis
* Fahimeh Rezaei
* Rakshith Raj Gurupura Puttaraju
* Hasan Ul Islam Shaffy
* Mary Acquah


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mrmajumder/contestIO.svg?style=for-the-badge
[contributors-url]: https://github.com/mrmajumder/contestIO/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mrmajumder/contestIO.svg?style=for-the-badge
[forks-url]: https://github.com/mrmajumder/contestIO/network/members
[stars-shield]: https://img.shields.io/github/stars/mrmajumder/contestIO.svg?style=for-the-badge
[stars-url]: https://github.com/mrmajumder/contestIO/stargazers
[issues-shield]: https://img.shields.io/github/issues/mrmajumder/contestIO.svg?style=for-the-badge
[issues-url]: https://github.com/mrmajumder/contestIO/issues
[license-shield]: https://img.shields.io/github/license/mrmajumder/contestIO.svg?style=for-the-badge
[license-url]: https://github.com/mrmajumder/contestIO/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/monsieurmajumder
[youtube-shield]: https://img.shields.io/badge/Video%20Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white
[github-url]: https://github.com/MrMajumder/
[email]: mailto:monsieurmajumder@gmail.com
[website-url]: https://mrmajumder.github.io/