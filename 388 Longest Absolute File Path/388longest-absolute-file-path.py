class Solution:
    def lengthLongestPath(self, input: str) -> int:
        subdirs = []
        subdir_len = 0
        max_len = 0

        for blob in input.split('\n'):
            # Check if it's a file or extension
            # Check number of tabs
            items = blob.split('\t')
            tabs_count = len(items) - 1
            
            # Check the new indentation level
            dirs_to_remove = len(subdirs) - tabs_count

            if dirs_to_remove > 0:
                subdir_len -= sum(x for x in subdirs[tabs_count:]) + dirs_to_remove
            del subdirs[tabs_count:]
            
            file_or_dir = items[-1]
            file_or_dir_len = len(file_or_dir)
            if "." in file_or_dir:
                # File, compare and update max_len
                max_len = max(max_len, subdir_len + file_or_dir_len)
            else:
                # Directory, update subdirs and subdir_len
                subdirs.append(file_or_dir_len)
                subdir_len += 1 + file_or_dir_len
            
        return max_len