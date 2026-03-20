# Team Details
Team Name: **CodeManthan**  
Members:
- Tvisha (Team Lead – Project Planning, Coordination, Documentation)  
- Rashi (System Design, Backend Logic, AI Integration)  
- Gurudutt (Frontend Development, UI/UX Design, Presentation)

---

# Gig-Guard
An AI-enabled parametric insurance platform that safeguards gig workers against income loss caused by external disruptions such as extreme weather or environmental conditions.

---

## Persona & Scenario

### Persona:
Rahul, a food delivery partner, earns per order and works daily to sustain his income.

### Problem Scenario:
- Heavy rain / high AQI / curfew → Rahul cannot deliver orders  
- No work → No income  
- No existing protection system  

### Our Solution:
Gig-Guard ensures Rahul receives automatic compensation when such disruptions occur.

---

## Features

+ **Weekly Subscription Model** – Simple and affordable insurance plans designed specifically for delivery workers  
+ **Automatic Payout System** – No manual claims; payouts are triggered instantly based on predefined conditions  
+ **Intelligent Trigger Engine** – Uses real-time data from weather, AQI, and local disruption sources to monitor conditions and activate payouts  
+ **AI-Based Premium Calculation** – Adjusts weekly premium based on location risk and historical disruption data  
+ **Fraud Detection Mechanism** – Identifies suspicious patterns and prevents false claims  
+ **User Dashboard** – Displays active plan, earnings protected, and claim history  
+ **Lightweight Web Access** – Accessible on any device without installation  

---

## System Workflow

![WhatsApp Image 2026-03-20 at 2 22 51 AM](https://github.com/user-attachments/assets/a65bf5ce-c963-4c79-9659-0b04808675f9)

---

## Weekly Premium Model

+ Users pay a fixed weekly premium  
+ Premium depends on:  
  - Location risk  
  - Historical disruption data  
  - Work patterns  

+ Higher risk → higher premium  
+ Lower risk → lower premium  

### Example:
- Low Risk → ₹20/week  
- Medium Risk → ₹40/week  
- High Risk → ₹70/week  

---

## Parametric Triggers

Payouts are triggered automatically when:

+ Rainfall exceeds threshold  
+ AQI crosses hazardous level  
+ Curfew or restriction in area  
+ Platform/service downtime  

---

## AI/ML Integration

+ **Premium Calculation**: Uses location, weather history, and activity data to generate a risk score (0–1) and adjust pricing  
+ **Fraud Detection**: Detects unusual activity, fake claims, and abnormal patterns using behavior analysis  

---

## Platform Choice: Web Application

We chose a web application because:

+ Easy accessibility across devices  
+ No installation required  
+ Faster deployment and testing  
+ Works well even on low-end devices  

---

## Tech Stack

+ Frontend: HTML, CSS, JavaScript (React optional)  
+ Backend: Node.js / Python (Flask)  
+ Database: MongoDB / MySQL  
+ APIs: Weather API, AQI API  

---

## Development Plan

+ Phase 1: Ideation, workflow, documentation  
+ Phase 2: Core feature development  
+ Phase 3: AI and fraud detection improvements  

---

## Adversarial Defense & Anti-Spoofing Strategy

### Differentiation
Gig-Guard does not rely solely on GPS data. It uses a multi-layer AI-based verification system to differentiate between genuine users and spoofers.

+ **Behavior Analysis** – Real users show consistent movement patterns, while spoofers show unnatural jumps  
+ **Activity Validation** – Checks delivery activity, app usage logs, and working patterns  
+ **Anomaly Detection (AI)** – Compares current behavior with historical data  

---

### The Data

1. Device Sensors  
+ Accelerometer (movement detection)  
+ Gyroscope (motion consistency)  

2. Network & Location Data  
+ GPS + IP consistency  
+ Cell tower signals  

3. User Activity Data  
+ Delivery history  
+ App usage patterns  
+ Active working hours  

4. Environmental Validation  
+ Weather API  
+ AQI data  
+ Area-wide disruptions  

5. Cluster Detection  
If multiple users show identical suspicious behavior, the system flags a potential fraud ring.

---

### UX Balance

1. Risk-Based Claim Handling  
+ Low risk → Instant payout  
+ Medium risk → Auto-check with slight delay  
+ High risk → Manual review  

2. Grace Handling  
+ Temporary GPS/network issues are tolerated  
+ No immediate rejection  

3. Transparency  
+ Users are informed if claim is under review  
+ No hidden penalties  

4. Trust Score System  
+ Users build reliability over time  
+ High-trust users get faster approvals  

---
