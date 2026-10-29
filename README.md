# Inventory programming labs

- Repository root: Lab 06 object-oriented inventory application, tests, UML diagram,
  assignment PDF and its own `inventory.json`.
- `modular/`: earlier procedural and modular auditor labs, text inventory,
  JSON inventory and existing lab log.

Run Lab 06 from this folder:

```powershell
python inventory_manager.py
python -B -m unittest -v test_lab06
```

Run earlier labs from their folder so their relative data paths resolve:

```powershell
cd modular
python persistent_auditor.py
```

Run Lab 06 in the existing Docker image with mounted source:

```powershell
docker run --rm -it -v "${PWD}:/app" -w /app inf1103-labs-smart-auditor
```

The root Dockerfile builds the OOP version, including its initial inventory.
The root application and `modular/` have separate inventory data so changes in one version do not
affect the other. Git metadata and configuration stay at the repository root.
