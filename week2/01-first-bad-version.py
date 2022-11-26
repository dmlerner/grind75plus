def isBadVersion(x):
    return True

def first_bad_version(n):
    lowest_possible_version = 1 # inclusive
    highest_possible_version = n # inclusive
    # invariant: answer is somewhere [lowest_possible_version, highest_possible_version]

    while lowest_possible_version < highest_possible_version:
        version_to_check = (lowest_possible_version + highest_possible_version)//2
        if isBadVersion(version_to_check):
            # not - 1 because version_to_check could be the first_bad_version
            highest_possible_version = version_to_check
        else:
            lowest_possible_version = version_to_check + 1
    assert lowest_possible_version == highest_possible_version
    if isBadVersion(lowest_possible_version):
        return lowest_possible_version
    # return isBadVersion(lowest_possible_version)
