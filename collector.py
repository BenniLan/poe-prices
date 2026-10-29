import requests, pandas as pd, datetime as dt, os

BASE = "https://poe.ninja/poe1/api/economy"
HEADERS = {"User-Agent": "student-ml-project (https://github.com/BenniLan/poe-prices)"}
OUT = "ninja_snapshots.csv"

def get(path, **params):
    r = requests.get(f"{BASE}/{path}", params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()

league_id = get("leagues")[0]["id"]
data = get("exchange/current/overview", league=league_id, type="Currency")

items = data["core"]["items"]
names = ({i["id"]: i["name"] for i in items} if isinstance(items, list)
         else {k: v.get("name") for k, v in items.items()})

now = dt.datetime.now(dt.timezone.utc).isoformat()
snap = pd.DataFrame([{
    "time": now, "league": league_id, "primary": data["core"]["primary"],
    "id": l["id"], "name": names.get(l["id"]),
    "primaryValue": l["primaryValue"],
    "volumePrimaryValue": l["volumePrimaryValue"],
} for l in data["lines"]])

snap.to_csv(OUT, mode="a", index=False, header=not os.path.exists(OUT))
print(f"saved {len(snap)} rows at {now} for {league_id}")