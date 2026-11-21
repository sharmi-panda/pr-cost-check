import pytest
from pr_cost_check.estimator import ClusterConfig, cost_per_run

def test_cost_per_run_simple():
    config = ClusterConfig(workers=3, dbu_per_node_hour=1.0,
                           vm_price_per_node_hour=0.5, dbu_rate=0.2)
    # 4 nodes for 2 hours: DBU cost 1.6 plus VM cost 4.0
    assert cost_per_run(config, hours=2) == pytest.approx(5.6)