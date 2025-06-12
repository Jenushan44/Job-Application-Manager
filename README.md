# Job Application Manager 

A desktop tool that is built with Python and Tkinter to help track your job applications. Add details like company, role, status, date, salary, notes and save everything locally.

## Table Of Contents 

- [Motivation](#motivation)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Motivation 

I created this project to stay organized while applying for internships and jobs. Instead of relying on messy spreadsheets, this app provides a focused and lightweight way to log applications, attach resumes and track progress. 

## Features 

- Add, edit, and delete job applications
- Track title, company, salary, date, status and notes
- Attach and open PDF resumes
- Status options: Applied, Rejected, Accepted
- Data saved locally in "jobs.json" file

## Technologies Used 

- Python 3
- Tkinter (GUI)
- tkcalendar (date selection)
- json (saving job data)
- webbrowser & filedialog (resume handling)

## Installation 

1. Clone the repository
```
bash
git clone https://github.com/yourusername/job-application-manager.git
cd job-application-manager
```

2. Install packages
```
pip install tkcalendar
```

3. Run the app
```
python JobAppManager.py
```

## Usage 
- Fill in job details
- Click Browse to attach a resume (PDF)
- Choose your application status
- Add any personal notes
- Press Save to store the job
- Your data will be saved locally in jobs.json
