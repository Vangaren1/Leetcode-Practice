from typing import Optional, List
import string


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:

        validBusiness = {
            "electronics": [],
            "grocery": [],
            "pharmacy": [],
            "restaurant": [],
        }

        results = []
        for index, coup in enumerate(code):
            if (not coup.replace("_", "").isalnum()) and coup != "_":
                continue
            busi = businessLine[index]
            if busi not in validBusiness.keys():
                continue
            if isActive[index]:
                validBusiness[busi].append(coup)

        for key, val in validBusiness.items():
            validBusiness[key].sort()
            results += validBusiness[key]

        return results


if __name__ == "__main__":
    sol = Solution()

    code = ["2", "E", "Q", "w", "m", "V", "j", "s", "c", "_", "V", "T"]
    businessLine = [
        "pharmacy",
        "electronics",
        "pharmacy",
        "invalid",
        "invalid",
        "pharmacy",
        "pharmacy",
        "electronics",
        "restaurant",
        "grocery",
        "grocery",
        "invalid",
    ]
    isActive = [
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        True,
        False,
        False,
    ]

    print(sol.validateCoupons(code, businessLine, isActive))
    print("Running Solution...")
