# **Gig-Guard**
An AI-enabled parametric insurance platform that safeguards gig workers against income loss caused by external disruptions such as extreme weather or environmental conditions.

---

## Persona & Scenario
#### **Persona:**
Rahul, a food delivery partner, earns per order and works daily to sustain his income.
### **Problem Scenario:**
- Heavy rain / high AQI / curfew → Rahul cannot deliver orders
- No work → No income
- No existing protection system
### **Our Solution:**
Gig-Guard ensures Rahul receives automatic compensation when such disruptions occur.

---

## Features
+ **Weekly Subscription Model** – Simple and affordable insurance plans designed specifically for delivery workers.
+ **Automatic Payout System** – No manual claims; payouts are triggered instantly based on predefined conditions.
+ **Intelligent Trigger Engine** – Uses real-time data from weather, AQI, and local disruption sources to continuously monitor conditions and automatically activate payouts when predefined risk thresholds are crossed
+ **AI-Based Premium Calculation** – Adjusts weekly premium based on location risk and historical disruption data.
+ **Fraud Detection Mechanism** – Identifies suspicious patterns and prevents false claims.
+ **User Dashboard** – Displays active plan, earnings protected, and claim history in a simple interface.
+ **Lightweight Web Access** – Accessible on any device without installation, optimized for ease of use.

---

## Weekly Premium Model
+	Users pay a fixed weekly premium
+	Premium depends on:  
  Location risk  
 Historical disruption data  
 Work patterns  
+ Higher risk → higher premium  
+ Lower risk → lower premium

---

## Parametric Triggers
Payouts are triggered automatically when:
+	Rainfall exceeds threshold
+	AQI crosses hazardous level
+	Curfew or restriction in area
+	Platform/service downtime

---

## AI/ML Integration
+ Premium Calculation: Predicts risk and adjusts pricing
+ Fraud Detection: Detects unusual activity and fake claims

---

## Platform Choice: Web Application
+	We chose a web application because:
+	Easy accessibility across devices
+	No installation required
+	Faster deployment and testing
+	Works well even on low-end devices

---

### Tech Stack
+	Frontend: HTML, CSS, JavaScript (React optional)
+	Backend: Node.js / Python (Flask)
+	Database: MongoDB / MySQL
+	APIs: Weather API, AQI API

---

### Development Plan
+	Phase 1: Ideation, workflow, documentation
+	Phase 2: Core feature development
+	Phase 3: AI + fraud detection improvements

---

## Adversarial Defense & Anti-Spoofing Strategy
### Differentiation (Real vs Fake Users)
GigGuard does not rely solely on GPS data. Instead, it uses a multi-layer verification system powered by AI to differentiate between genuine users and spoofers.
+ Behavior Analysis
Real users show consistent movement patterns (active deliveries, route changes), while spoofers show static or unnatural jumps in location.
+ Activity Validation
Genuine delivery partners have:
+ Recent order activity
+ App interaction logs
+ Continuous usage patterns
+ Anomaly Detection (AI)
Machine learning models compare current behavior with historical patterns to detect unusual claims.
