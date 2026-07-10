# Agent Router Routing Rules

## Purpose

This document defines how Agent Router selects and sequences AI agents based on user requests.

The objective is to ensure consistent, efficient and scalable task routing.

---

# Routing Process

```
Receive Request

↓

Intent Analysis

↓

Task Classification

↓

Agent Selection

↓

Dependency Check

↓

Execution Plan

↓

Send to Orchestrator
```

---

# Single-Agent Routing

## SEO Tasks

Route to:

- SEOAgent

Examples:

- Keyword research
- Technical SEO audit
- Meta title optimization

---

## Content Tasks

Route to:

- ContentAgent

Examples:

- Blog writing
- Product descriptions
- Email campaigns

---

## Meta Ads Tasks

Route to:

- MetaAdsAgent

Examples:

- Campaign optimization
- Audience analysis
- ROAS improvement

---

## Analytics Tasks

Route to:

- AnalyticsAgent

Examples:

- KPI analysis
- Revenue trends
- Funnel analysis

---

## Store Tasks

Route to:

- IdeaSoftAgent

Examples:

- Product management
- Store audit
- Category optimization

---

## Strategy Tasks

Route to:

- CEOAgent

Examples:

- Business planning
- Growth strategy
- Resource allocation

---

## Reporting Tasks

Route to:

- ReportingAgent

Examples:

- Weekly reports
- KPI dashboard
- Executive summary

---

# Multi-Agent Routing

## SEO Blog

Execution Order:

1. SEOAgent
2. ContentAgent
3. ReportingAgent

---

## Store Audit

Execution Order:

1. IdeaSoftAgent
2. SEOAgent
3. AnalyticsAgent
4. ReportingAgent

---

## Marketing Campaign

Execution Order:

1. CEOAgent
2. MetaAdsAgent
3. AnalyticsAgent
4. ReportingAgent

---

## Product Launch

Execution Order:

1. CEOAgent
2. ContentAgent
3. SEOAgent
4. IdeaSoftAgent
5. MetaAdsAgent
6. ReportingAgent

---

# Conflict Resolution

If multiple agents can perform a task:

- Select the most specialized agent.
- Minimize overlap.
- Preserve execution quality.

---

# Priority Rules

Priority levels:

- Critical
- High
- Medium
- Low

Determine priority based on:

- Business impact
- Customer impact
- Revenue impact
- Operational urgency

---

# Output Requirements

Every routing decision must specify:

- User Intent
- Selected Agents
- Execution Order
- Estimated Complexity
- Expected Deliverables

---

# Core Principle

Route every request through the smallest, most effective set of agents while maintaining high-quality outcomes.

---

# Version

v0.1 Foundation