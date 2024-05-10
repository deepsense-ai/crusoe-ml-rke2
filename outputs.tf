output "rke-headnode-instance_public_ip" {
  value = crusoe_compute_instance.rke_headnode[0].network_interfaces[0].public_ipv4.address
}

output "rke-ingress-instance_public_ip" {
  value = local.ingress_interface.public_ipv4.address
}
