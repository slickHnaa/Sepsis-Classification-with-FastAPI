# 🚀Sepsis-Classification-with-FastAPI 🚀

## Project Description 
This project is focused on the classification of sepsis cases using the FastAPI framework. Sepsis is a critical medical condition that requires prompt identification and treatment.






This project aims to provide a streamlined solution to classify sepsis cases quickly and effectively.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Data](#data)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Future Work](#future-work)
- [Contact](#contact)

## Project Overview

The "Sepsis Classification with FastAPI" project aims to develop a classification system for sepsis cases using the FastAPI framework. Sepsis is a life-threatening condition that requires immediate medical attention. This project addresses the critical need for timely identification and classification of sepsis cases to facilitate prompt treatment and improve patient outcomes.

The objectives of the project are as follows:

1. Train a machine learning model on a diverse dataset of sepsis cases to accurately predict the likelihood of sepsis in patients.

2. Utilize the FastAPI framework to create a user-friendly and efficient web interface for healthcare professionals to interact with the sepsis classification model.

3. Improve diagnostic capabilities by achieving high accuracy, sensitivity, and specificity in sepsis classification.

4. Provide a comprehensive and scalable solution that can be easily deployed in real-time healthcare environments.

### i. Description of dataset <a name="dataset"></a>

<table>
  <tr>
    <th>Column Name</th>
    <th>Attribute/Target</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>ID</td>
    <td>N/A</td>
    <td>Unique number to represent patient ID</td>
  </tr>
  <tr>
    <td>PRG</td>
    <td>Attribute1</td>
    <td>Plasma glucose</td>
  </tr>
  <tr>
    <td>PL</td>
    <td>Attribute 2</td>
    <td>Blood Work Result-1 (mu U/ml)</td>
  </tr>
  <tr>
    <td>PR</td>
    <td>Attribute 3</td>
    <td>Blood Pressure (mm Hg)</td>
  </tr>
  <tr>
    <td>SK</td>
    <td>Attribute 4</td>
    <td>Blood Work Result-2 (mm)</td>
  </tr>
  <tr>
    <td>TS</td>
    <td>Attribute 5</td>
    <td>Blood Work Result-3 (mu U/ml)</td>
  </tr>
  <tr>
    <td>M11</td>
    <td>Attribute 6</td>
    <td>Body mass index (weight in kg/(height in m)^2)</td>
  </tr>
  <tr>
    <td>BD2</td>
    <td>Attribute 7</td>
    <td>Blood Work Result-4 (mu U/ml)</td>
  </tr>
  <tr>
    <td>Age</td>
    <td>Attribute 8</td>
    <td>Patients age (years)</td>
  </tr>
  <tr>
    <td>Insurance</td>
    <td>N/A</td>
    <td>If a patient holds a valid insurance card</td>
  </tr>
  <tr>
    <td>Sepssis</td>
    <td>Target</td>
    <td>Positive: if a patient in ICU will develop sepsis, and Negative: otherwise</td>
  </tr>
</table>