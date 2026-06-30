import threading
import subprocess
import time

class ProcessMonitor():
    def __init__(self):
        self.status = {
                "ur20": False,
                "nex10": False,
                "rgt_manager": False,
                "foxglove_bridge": False,
                "tool_side_realsense": False,
                "bed_side_realsense": False,
                "gelsight": False,
                "thermal_camera": False,
                "audio_capture": False,
                }
        self.stop_event = threading.Event()
        self.thread = None

    def start(self):
        self._thread = threading.Thread(target=self.update_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self.stop_event.set()

    def update_loop(self):
        while not self.stop_event.is_set():
            node_list = self.run_command("ros2 node list", 5)
            if "/ur20/ur20" in node_list:
                self.status["ur20"] = self.check_command_output("ros2 topic echo /ur20/io_and_status_controller/safety_mode --once", "mode: 1", 5)
            else:
                self.status["ur20"] = False
            if "/nex10/nex10" in node_list:
                self.status["nex10"] = self.check_command_output("ros2 control list_hardware_components -c /nex10/controller_manager", "nex10_joint_1/position [available]", 5)
            else:
                self.status["nex10"] = False
            if "rgt_manager" in node_list:
                self.status["rgt_manager"] = True
            else:
                self.status["rgt_manager"] = False
            if "foxglove_bridge" in node_list:
                self.status["foxglove_bridge"] = True
            else:
                self.status["foxglove_bridge"] = False
            if "tool_side_realsense" in node_list:
                self.status["tool_side_realsense"] = True
            else:
                self.status["tool_side_realsense"] = False
            if "bed_side_realsense" in node_list:
                self.status["bed_side_realsense"] = True
            else:
                self.status["bed_side_realsense"] = False
            if "gelsight" in node_list:
                self.status["gelsight"] = True
            else:
                self.status["gelsight"] = False
            if "thermal_camera" in node_list:
                self.status["thermal_camera"] = True
            else:
                self.status["thermal_camera"] = False
            if "audio_capture" in node_list:
                self.status["audio_capture"] = True
            else:
                self.status["audio_capture"] = False
            time.sleep(1)
    
    def get_status(self):
        return self.status

    def run_command(self, command, timeout_seconds):
        try:
            result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=timeout_seconds
                    )
            return result.stdout
        except subprocess.TimeoutExpired:
            return ""
        except:
            return ""

    def check_command_output(self, command, search_string, timeout_seconds):
        stdout = self.run_command(command, timeout_seconds)
        if search_string in stdout:
            return True
        else:
            return False

process_monitor = ProcessMonitor()
