# Proposal: Engineer Needed for SMS Pickup Scheduling MVP
**Job:** https://www.upwork.com/jobs/Engineer-Needed-for-SMS-Pickup-Scheduling-MVP-App_~022020878076558928544/
**Client:** USA, Verified, $40K+ spent, 5.0⭐

---

Hi! I read your requirements carefully — this is a clean, focused MVP and I love that approach. No overengineering, just a reliable SMS workflow that works.

**Here's how I'd architect it:**
I actually built a demo showing exactly this system:
→ https://digit500.github.io/sms-pickup-scheduling-demo/

Architecture: Twilio webhooks → Node.js/Express backend → PostgreSQL → Slack/email notifications to ops team. Stateless, simple, HIPAA-conscious data handling.

**Key decisions:**
- Twilio for two-way SMS + webhooks (conversation state managed server-side)
- Calendly-style time slot logic built custom (more control, no extra dependency)
- PostgreSQL for pickup requests + status tracking
- Slack webhook for real-time ops notifications

**Timeline:** Functional MVP in 5 days, production-ready in 10.

**Relevant experience:**
- Twilio SMS/voice integrations
- Backend APIs (Node.js, Python, TypeScript)
- Webhook-driven architectures
- Healthcare-adjacent projects (data sensitivity awareness)

Available immediately, full capacity for the next 14 days.

Best,
Nedim — United DigiArt Vision
