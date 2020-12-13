
import subprocess

# ----------------------------------------------------------------------------
def exec_subprocess(cmd, return_output=False):
    """Execute the given command as a subprocess (blocking)
       Returns one off:
           - exit code of the command
           - stdout and stderr
           - -1 indicates an exception"""
    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = proc.communicate()
        if return_output:
            return (out, err)
        return proc.returncode
    except OSError:
        return -1

# ----------------------------------------------------------------------------
def has_nvidia_support():
    """Check if the instance has Nvida capabilities"""
    try:
        pci_info, errors = exec_subprocess(['lspci'], True)
    except TypeError:
        logging.info(
            'lspci command not found, instance Nvidia support cannot '
            'be determined'
        )
        return False

    if 'NVIDIA' in pci_info.decode():
        logging.info('Instance has Nvidia support')
        return True

    return False