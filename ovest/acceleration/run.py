

def run():
    mpi_init()
    while True:
        sig = get_signal()
        is_fall = falldetection(sig)


def get_is_fall():
    return is_fall


def test():
    print("acceleration")
