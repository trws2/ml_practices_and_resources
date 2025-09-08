def compute_efficiency(n_experts, k_active, d_in, d_out):
    # dense layers
    d = n_experts * d_in * d_out

    # moe flops
    m = k_active * d_in * d_out

    # savings
    return 100 * (d - m) / (1.0 * d)

