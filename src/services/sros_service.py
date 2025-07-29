from pysros.management import connect
from pysros.exceptions import ModelProcessingError
from pysros.wrappers import Leaf
import asyncio

async def add_ip_prefix(prefix_name: str, ip_prefix: str):
    try:
        conn = connect(host="192.168.9.2",
                       username="admin",
                       password="T9x$7Qm@4Zp!Lk2GhRw6",
                       hostkey_verify=False)
        path = f'/nokia-conf:configure/filter/match-list/ip-prefix-list[prefix-list-name="nat-destination"]'
        payload = {
            'prefix-list-name': Leaf(prefix_name),
            'prefix': {ip_prefix: ({'ip-prefix': Leaf(ip_prefix)})}
        }
        conn.candidate.set(path, payload)
        conn.candidate.commit()  # Ensure to commit the changes
    except RuntimeError as error1:
        print("Connection failed:", error1)
        return {"error": str(error1)}
    except ModelProcessingError as error2:
        print("Failed to create the model-driven schema", error2)
        return {"error": str(error2)}
    return {"status": "success", "message": f"IP prefix {ip_prefix} added successfully."}

async def delete_ip_prefix(prefix_name: str, ip_prefix: str):
    try:
        conn = connect(host="127.0.0.1",
                       username="admin",
                       password="T9x$7Qm@4Zp!Lk2GhRw6",
                       hostkey_verify=False)
        path = f'/nokia-conf:configure/filter/match-list/ip-prefix-list[prefix-list-name="{prefix_name}"]/prefix[ip-prefix="{ip_prefix}"]'
        conn.candidate.delete(path)
        conn.candidate.commit()  # Ensure to commit the changes
    except RuntimeError as error1:
        print("Connection failed:", error1)
        return {"error": str(error1)}
    except ModelProcessingError as error2:
        print("Failed to create the model-driven schema", error2)
        return {"error": str(error2)}
    return {"status": "success", "message": f"IP prefix {ip_prefix} deleted successfully."}