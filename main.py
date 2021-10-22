if __name__ == '__main__':
    process_list_ = [
        {"process_name": "a.exe", "pid": 420, "parent_pid": 428},
        {"process_name": "c.exe", "pid": 428, "parent_pid": None},
        {"process_name": "d.exe", "pid": 551, "parent_pid": 420},
        {"process_name": "e.exe", "pid": 552, "parent_pid": 428},
        {"process_name": "f.exe", "pid": 553, "parent_pid": None},
        {"process_name": "g.exe", "pid": 4, "parent_pid": 553},
        {"process_name": "b.exe", "pid": 7, "parent_pid": 4},
        {"process_name": "h.exe", "pid": 11, "parent_pid": 7}
    ]

    proc_dict_ = dict()


    def populate_proc_dict():
        for proc_ in process_list_:
            if proc_["pid"] not in proc_dict_:
                proc_dict_[proc_["pid"]] = list()
            parent_id_ = proc_["parent_pid"]
            if parent_id_ in proc_dict_:
                children_ = proc_dict_.get(parent_id_, [])
                children_ += [proc_]
            else:
                proc_dict_[parent_id_] = [proc_]


    populate_proc_dict()


    def print_tree(proc_lst, level):
        for proc in proc_lst:
            s = '-' * level * 3
            print(s + proc["process_name"])
            next_children = proc_dict_[proc["pid"]]
            print_tree(next_children, level + 1)

    # Start printing from the roots (processes with None as parent)
    print_tree(proc_dict_[None], 0)
