from dataclasses import dataclass

@dataclass
class ClusterConfig:
    workers: int
    dbu_per_node_hour: float       # from Databricks docs for the node type
    vm_price_per_node_hour: float  # from the cloud's price list
    dbu_rate: float                # price per DBU for the compute type

def cost_per_run(config: ClusterConfig, hours: float) -> float:
    nodes = config.workers + 1  # workers plus one driver
    dbu_cost = nodes * config.dbu_per_node_hour * hours * config.dbu_rate
    vm_cost = nodes * config.vm_price_per_node_hour * hours
    return dbu_cost + vm_cost