from fastapi import APIRouter, HTTPException
import tmux
from models import StartProcessRequest, StopProcessRequest
from process_monitor import process_monitor

router = APIRouter()

@router.get("/status")
def get_status():
    windows = tmux.get_windows()
    process_status = process_monitor.get_status()
    status = {
            "ur20": "unkown",
            "nex10": "unkown",
            "rgt_manager": "unkown",
            "foxglove_bridge": "unkown",
            }
    for process_name in status:
        if process_name in windows and process_status[process_name] == True:
            status[process_name] = "running"
        elif process_name in windows and process_status[process_name] == False:
            status[process_name] = "started"
        elif process_name not in windows and process_status[process_name] == False:
            status[process_name] = "stopped"
        else:
            status[process_name] = "unknown"
    return status

@router.post("/start")
def start_process(req: StartProcessRequest):
    if req.name == "ur20":
        use_mock_hardware = bool((req.params or {}).get("use_mock_hardware", False))
        command = f"ros2 launch ur_bringup bringup.launch.py ns:=ur20 use_mock_hardware:={use_mock_hardware}"
        tmux.start_process(req.name, command)
    elif req.name == "nex10":
        use_mock_hardware = bool((req.params or {}).get("use_mock_hardware", False))
        use_ft_sensor = bool((req.params or {}).get("use_ft_sensor", False))
        command = f"ros2 launch ynx_bringup bringup.launch.py ns:=nex10 use_ft_sensor:={use_ft_sensor} use_mock_hardware:={use_mock_hardware}"
        tmux.start_process(req.name, command)
    elif req.name == "rgt_manager":
        command = "ros2 run rgt_manager rgt_manager"
        tmux.start_process(req.name, command)
    elif req.name == "foxglove_bridge":
        command = "ros2 run foxglove_bridge foxglove_bridge"
        tmux.start_process(req.name, command)
    else:
        raise HTTPException(status_code=404, detail=f"Process '{req.name}' is not recognized.")

    return {"status": "started", "name": req.name}

@router.post("/stop")
def stop_process(req: StopProcessRequest):
    if req.name == "ur20":
        tmux.stop_process(req.name)
    elif req.name == "nex10":
        tmux.stop_process(req.name)
    elif req.name == "rgt_manager":
        tmux.stop_process(req.name)
    elif req.name == "foxglove_bridge":
        tmux.stop_process(req.name)
    else:
        raise HTTPException(status_code=404, detail=f"Process '{req.name}' is not recognized.")

    return {"status": "stopped", "name": req.name}
