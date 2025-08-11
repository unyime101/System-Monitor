# 🖥️ System Resource Monitor (Python)

A simple system monitoring tool built in Python for tracking CPU, memory, disk usage, and system uptime — with optional alerting.

---

## 📌 Project Overview

This project is part of my journey to deepen my knowledge of **Python programming**, and to gain hands-on experience with **system monitoring**, **logging**, and **automation**.

The script runs on my **Raspberry Pi 5 (4GB RAM)** using **Ubuntu Linux**, but is portable to most Linux environments.

---

## 🚧 Current Progress

| Area                      | Status        | Notes                                                                 |
|---------------------------|---------------|-----------------------------------------------------------------------|
| Python monitoring script  | ✅Completed   | Script created                                                        |
| Logging to text file      | ✅Completed   | Implemented basic logging with timestamps                             |
| Alert thresholds          | ✅Completed   | Added conditional checks and alerting. Also for planned downtimes     |
| Cron automation           | ✅Completed   | Used `cron` to automate execution                                     |
| Project documentation     | ✅ Completed  | README created                                                        |
| Git setup with .gitignore | ✅ Completed  | Basic `.gitignore` setup finished                                     |
| GitHub publishing         | 🚧 In Progress| Will push to GitHub with version control                              |
| Email/Slack alerts        | ✅ Completed  | Integrated messaging alerts for high usage and on boot.               |
| Grafana/Prometheus logging| 🔜 Planned    | Future step: push data to a metrics database                          |
| Docker/Kubernetes         | 🔜 Planned    | Will containerize and run on Minikube cluster                         |

---

## 📊 Features

- ✅  Logs **CPU usage** (%)
- ✅ Logs **Memory usage** (%)
- ✅ Logs **Disk usage** (%)
- ✅ Logs **System uptime**
- ✅ Triggers alerts if usage crosses thresholds
- ✅ Outputs logs to a text file (`system_log.txt`)
- ✅ Can be scheduled with `cron` for automated monitoring
- ✅ Sends email alerts on boot and when thressholds are exceeded
---

## 🧠 Learning Goals
- Strengthen Python skills by building practical automation tools
- Learn system health monitoring and log management on Linux
- Resource used to research sytem utils, psutil: https://pypi.org/project/psutil/
- Explore alerting, scheduling, and observability principles
- Resource used to research cron automation: https://www.freecodecamp.org/news/cron-jobs-in-linux/
- Resource used to research Email alerts smtplb: https://realpython.com/python-send-email/
