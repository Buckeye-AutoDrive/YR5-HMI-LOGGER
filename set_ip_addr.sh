#!/usr/bin/env bash
set -euo pipefail

run_ip() {
  if [[ "${EUID}" -eq 0 ]]; then
    ip "$@"
  else
    sudo ip "$@"
  fi
}

if ! ip -4 addr show dev lo | grep -q '192\.168\.69\.10/24'; then
  run_ip addr add 192.168.69.10/24 dev lo
fi

if ! ip -4 addr show dev lo | grep -q '192\.168\.69\.69/24'; then
  run_ip addr add 192.168.69.69/24 dev lo
fi

run_ip route replace 192.168.69.69/32 dev lo src 192.168.69.10
echo "Configured loopback aliases for local Intel/HMI emulation."s