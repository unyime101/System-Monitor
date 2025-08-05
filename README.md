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
| Python monitoring script  | 🚧 In Progress | Currently being written and tested                                    |
| Logging to text file      | 🚧 In Progress | Implementing basic logging with timestamps                           |
| Alert thresholds          | 🔜 Planned     | Add conditional checks and alerting                                  |
| Cron automation           | 🔜 Planned     | Will use `cron` to automate execution                                |
| Project documentation     | ✅ Completed   | README created                                                        |
| Git setup with .gitignore| ✅ Completed   | Basic `.gitignore` setup finished                                    |
| GitHub publishing         | 🔜 Planned     | Will push to GitHub with version control                             |
| Email/Slack alerts        | 🔜 Planned     | Will integrate messaging alerts for high usage                       |
| Grafana/Prometheus logging| 🔜 Planned     | Future step: push data to a metrics database                         |
| Docker/Kubernetes         | 🔜 Planned     | Will containerize and run on Minikube cluster                        |

---

## 📊 Features

- 🚧 Logs **CPU usage** (%)
- 🚧 Logs **Memory usage** (%)
- 🚧 Logs **Disk usage** (%)
- 🚧 Logs **System uptime**
- 🔜 Triggers alerts if usage crosses thresholds
- 🔜 Outputs logs to a text file (`system_log.txt`)
- 🔜 Can be scheduled with `cron` for automated monitoring

---

## 🧠 Learning Goals

- Strengthen Python skills by building practical automation tools
- Learn system health monitoring and log management on Linux
- Explore alerting, scheduling, and observability principles
