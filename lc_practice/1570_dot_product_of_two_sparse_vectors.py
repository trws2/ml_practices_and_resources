class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = {i: v for i, v in enumerate(nums) if v != 0}
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ret = 0
        if len(self.vec) > len(vec.vec):
            for i, v in vec.vec.items():
                if i in self.vec:
                    ret += v * self.vec[i]
        else:
            for i, v in self.vec.items():
                if i in vec.vec:
                    ret += v * vec.vec[i]
        return ret

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
