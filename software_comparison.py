"""
software_comparison.py
----------------------
Structured analysis and comparison of finance & accounting software platforms
based on 10+ years of hands-on usage across solar energy, retail manufacturing,
hotel, and transaction advisory industries.

Built by: Arjun D | Finance Head | 8+ ERP/accounting platforms
Context: Submitted as part of Terac expert panel application for finance
         software UX research study.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'


# ── Platform data: scored 1-5 on each dimension (5 = best) ──────────────────
PLATFORMS = [
    {
        "name": "Microsoft Dynamics 365",
        "category": "Enterprise ERP",
        "used_for": "Ciel Et Terre Solar — India subsidiary (IFRS consolidation, cross-border reporting)",
        "ease_of_use": 3,
        "reporting_power": 5,
        "automation": 4,
        "multi_entity": 5,
        "integration": 5,
        "mobile": 3,
        "implementation_complexity": 2,   # 2 = complex/hard (lower = harder)
        "cost": 2,                         # 2 = expensive
        "best_for": "Large multi-entity groups, IFRS consolidation, cross-border operations",
        "pain_points": "Complex configuration, long implementation, steep learning curve, expensive licensing",
        "standout_feature": "Seamless multi-entity consolidation; Power BI native integration",
    },
    {
        "name": "Oracle NetSuite",
        "category": "Cloud ERP",
        "used_for": "Transaction advisory — client due diligence reviews",
        "ease_of_use": 3,
        "reporting_power": 5,
        "automation": 4,
        "multi_entity": 5,
        "integration": 5,
        "mobile": 4,
        "implementation_complexity": 2,
        "cost": 2,
        "best_for": "Scaling SaaS/tech companies, multi-subsidiary, real-time financial visibility",
        "pain_points": "Customisation requires SuiteScript (developer knowledge), expensive for small orgs",
        "standout_feature": "Real-time consolidated dashboards; strong revenue recognition (ASC 606/IFRS 15)",
    },
    {
        "name": "SAP (FI/CO Modules)",
        "category": "Enterprise ERP",
        "used_for": "Ledger reviews during M&A due diligence at N.C.S. Raghavan & Co.",
        "ease_of_use": 2,
        "reporting_power": 5,
        "automation": 4,
        "multi_entity": 5,
        "integration": 5,
        "mobile": 3,
        "implementation_complexity": 1,
        "cost": 1,
        "best_for": "Multinational corporations, manufacturing, complex intercompany structures",
        "pain_points": "Extremely complex UI, requires dedicated SAP consultants, prohibitive cost for SMEs",
        "standout_feature": "Unmatched depth in cost centre / profit centre accounting and intercompany eliminations",
    },
    {
        "name": "Tally Prime",
        "category": "SME Accounting",
        "used_for": "Cotton World Group — daily accounting across 6 entities; statutory compliance",
        "ease_of_use": 5,
        "reporting_power": 3,
        "automation": 3,
        "multi_entity": 3,
        "integration": 2,
        "mobile": 2,
        "implementation_complexity": 5,
        "cost": 5,
        "best_for": "Indian SMEs, GST compliance, statutory reporting, fast daily bookkeeping",
        "pain_points": "Weak API/integration layer, limited BI capabilities, multi-entity management is cumbersome",
        "standout_feature": "Best-in-class Indian statutory compliance (GST, TDS, MCA); incredibly fast data entry",
    },
    {
        "name": "Xero",
        "category": "Cloud Accounting",
        "used_for": "Advisory firm clients — SME bookkeeping, payroll, bank reconciliation",
        "ease_of_use": 5,
        "reporting_power": 3,
        "automation": 5,
        "multi_entity": 2,
        "integration": 5,
        "mobile": 5,
        "implementation_complexity": 5,
        "cost": 4,
        "best_for": "SMEs, startups, freelancers; best bank-feed automation; 1000+ integrations",
        "pain_points": "Limited multi-entity/group consolidation; reporting is basic without add-ons",
        "standout_feature": "Best bank reconciliation UX in the market; Hubdoc integration for receipt capture",
    },
    {
        "name": "QuickBooks",
        "category": "Cloud Accounting",
        "used_for": "US-entity clients at advisory firm; global subsidiary accounting",
        "ease_of_use": 4,
        "reporting_power": 3,
        "automation": 4,
        "multi_entity": 2,
        "integration": 4,
        "mobile": 4,
        "implementation_complexity": 5,
        "cost": 4,
        "best_for": "US SMEs, self-employed professionals, simple multi-currency",
        "pain_points": "Weak multi-entity; payroll add-on pricing; customer support inconsistent",
        "standout_feature": "Best ecosystem for US tax compliance; strong A/R invoicing and payment collection",
    },
    {
        "name": "Zoho Books",
        "category": "Cloud Accounting",
        "used_for": "Indian startup clients — GST filing, invoicing, basic FP&A",
        "ease_of_use": 4,
        "reporting_power": 3,
        "automation": 4,
        "multi_entity": 3,
        "integration": 4,
        "mobile": 4,
        "implementation_complexity": 5,
        "cost": 5,
        "best_for": "Indian SMEs wanting Tally alternative with modern UI; best value for money",
        "pain_points": "Reporting less sophisticated than Xero/QBO; occasional bugs in GST return filing",
        "standout_feature": "Best-priced cloud accounting for Indian market; native Zoho CRM integration",
    },
    {
        "name": "IDS (Hotel ERP)",
        "category": "Hospitality ERP",
        "used_for": "Statutory audit of hotel clients — front office, F&B, room revenue reconciliation",
        "ease_of_use": 3,
        "reporting_power": 3,
        "automation": 3,
        "multi_entity": 2,
        "integration": 2,
        "mobile": 2,
        "implementation_complexity": 3,
        "cost": 3,
        "best_for": "Hotel and hospitality operations — PMS, POS, F&B, housekeeping all-in-one",
        "pain_points": "Finance module is secondary to operations; limited API connectivity; dated UI",
        "standout_feature": "Seamless night audit workflow; RevPAR and occupancy reporting built-in",
    },
]


def build_comparison_df(platforms: list) -> pd.DataFrame:
    """Build a comparison DataFrame from platform list."""
    rows = []
    dimensions = ["ease_of_use", "reporting_power", "automation",
                  "multi_entity", "integration", "mobile"]
    for p in platforms:
        row = {
            "Platform": p["name"],
            "Category": p["category"],
            "Used For": p["used_for"][:60] + "...",
        }
        for d in dimensions:
            row[d.replace("_", " ").title()] = p[d]
        row["Best For"] = p["best_for"][:80]
        row["Key Pain Point"] = p["pain_points"][:80]
        rows.append(row)
    return pd.DataFrame(rows)


def radar_chart(platforms: list, names: list, save_path: str = None):
    """Radar/spider chart comparing selected platforms."""
    categories = ["Ease of Use", "Reporting", "Automation", "Multi-Entity", "Integration", "Mobile"]
    N = len(categories)
    angles = [n / float(N) * 2 * 3.14159 for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    colors = ["#2C3E50", "#E74C3C", "#27AE60", "#3498DB", "#9B59B6", "#F39C12", "#1ABC9C", "#E67E22"]

    for i, name in enumerate(names):
        p = next(pl for pl in platforms if pl["name"] == name)
        values = [p["ease_of_use"], p["reporting_power"], p["automation"],
                  p["multi_entity"], p["integration"], p["mobile"]]
        values += values[:1]
        ax.plot(angles, values, "o-", linewidth=2, label=name, color=colors[i % len(colors)])
        ax.fill(angles, values, alpha=0.08, color=colors[i % len(colors)])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=11)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], size=8)
    ax.set_title("Finance Software Comparison — Radar Chart\n(5 = best)", size=13, fontweight="bold", y=1.08)
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.15), fontsize=9)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=150)
    else:
        plt.show()
    plt.close()


if __name__ == "__main__":
    df = build_comparison_df(PLATFORMS)
    print("Finance Software Platform Comparison:")
    print(df[["Platform", "Category", "Ease of Use", "Reporting Power",
              "Automation", "Multi Entity", "Integration"]].to_string(index=False))

    # Radar chart: Cloud accounting tools
    cloud_tools = ["Xero", "QuickBooks", "Zoho Books"]
    radar_chart(PLATFORMS, cloud_tools, save_path="cloud_accounting_radar.png")
    print("\nCloud accounting radar chart saved.")

    # Radar chart: Enterprise ERPs
    erp_tools = ["Microsoft Dynamics 365", "Oracle NetSuite", "SAP (FI/CO Modules)", "Tally Prime"]
    radar_chart(PLATFORMS, erp_tools, save_path="enterprise_erp_radar.png")
    print("Enterprise ERP radar chart saved.")
