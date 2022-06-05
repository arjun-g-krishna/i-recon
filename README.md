
# i Recon

An eye-blink based alert system for paralyzed patients suffering from ALS syndrome. 
Final year project done as part of APJ Abdul Kalam Technological University syllabus.

## Introduction

Several neurological disorders could cause patients to lose control over all voluntary muscles leaving them paralysed. 
The project puts forward a solution to the inconveniences faced by a paralyzed patient, making use of an alert mechanism to connect the caretaker with the patient.
It aims to provide round clock assistance with great efficiency.

## Run Locally

Clone the project

```bash
  git clone https://github.com/arjun-g-krishna/i-recon
```

Go to the project directory

```bash
  cd i-recon
```

Install dependencies

```bash
  pip install -r requirements.txt
```
> Replace "key.json" at line 14 in counter.py with the path to your firebase admin credentials json file and replace #### at line 15 with your firebase realtime database URL.

<br> Run the program

```bash
  python3 counter.py
```


## Authors

- [@arjun-g-krishna](https://www.github.com/arjun-g-krishna)
- [@abinbs](https://www.github.com/abinbs)
- [@AshikDavid](https://www.github.com/AshikDavid)
- [@Sarath-Kumar-S](https://www.github.com/Sarath-Kumar-S)

## Literature Review

 - [Efficient machine learning approach for volunteer eye-blink detection in real-time using webcam](https://doi.org/10.1016/j.eswa.2021.116073)
 - [Robust Eye Blink Detection Based on Eye Landmarks and Savitzky–Golay Filtering]( https://doi.org/10.3390/info9040093)
 - [Eye-Blink Detection System for Virtual Keyboard](https://ieeexplore.ieee.org/document/9428797)

