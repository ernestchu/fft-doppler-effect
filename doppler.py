c = 340
def v_receiver(f_observed, f_emitted, v_source):
    return (f_observed/f_emitted*(c+v_source)-c)
