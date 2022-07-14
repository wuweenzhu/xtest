from parameterized import parameterized
import warnings,json,csv
import codecs,os
import inspect as sys_inspect
from itertools import islice
from parameterized.parameterized import inspect
from functools import wraps
from parameterized.parameterized import reapply_patches_if_need
from parameterized.parameterized import delete_patches_if_need
from parameterized.parameterized import default_name_func
from parameterized.parameterized import skip_on_empty_helper
from parameterized.parameterized import default_doc_func
from parameterized import parameterized_class

def file_data(file=None,line=0):
    """
    数据文件参数化
    :param file:
    :return:
    """
    if file is None:
        raise FileNotFoundError("请指定数据文件")
    if os.path.isfile(file) is True:
        file_path = file
    # 遍历目录查找文件
    else:
        stack_t = sys_inspect.stack()
        ins = sys_inspect.getframeinfo(stack_t[1][0])
        file_dir = os.path.dirname(os.path.dirname(os.path.abspath(ins.filename)))
        file_path = None
        for root,dirs,files in os .walk(file_dir,topdown=False):
            for f in files:
                if f==file:
                    file_path =os.path.join(root,file)
                    break
            else:
                continue
            break

    file_type = file_path.split(".")[-1]

    if file_type == "json" :
        with open(file_path, "r") as load_f:
            load_dict = json.load(load_f)
            print(load_dict)
            return data(load_dict)

    elif file_type =="csv":
        load_csv = csv.reader(codecs.open(file_path,'r','utf_8_sig'))
        # 将csv格式的文件转成字典类型
        data_list = []
        for line in islice(load_csv,line,None):
            data_list.append(line)
        print(data_list)
        return data(data_list)


        # with open('data.csv', 'r') as f:
        #     reader = csv.reader(f)
        #     result = list(reader)
        #     print(result)
        #     return data(result)

    else:
        raise TypeError("文件类型不支持")



# class data(parameterized):
#     pass

def data(input, name_func=None, doc_func=None, skip_on_empty=False,
           **legacy):
    """ A "brute force" method of parameterizing test cases. Creates new
        test cases and injects them into the namespace that the wrapped
        function is being defined in. Useful for parameterizing tests in
        subclasses of 'UnitTest', where Nose test generators don't work.

        # >>> @parameterized.expand([("foo", 1, 2)])
        # ... def test_add1(name, input, expected):
        # ...     actual = add1(input)
        # ...     assert_equal(actual, expected)
        # ...
        # >>> locals()
        # ... 'test_add1_foo_0': <function ...> ...
        # >>>
        # """

    if "testcase_func_name" in legacy:
        warnings.warn("testcase_func_name= is deprecated; use name_func=",
                      DeprecationWarning, stacklevel=2)
        if not name_func:
            name_func = legacy["testcase_func_name"]

    if "testcase_func_doc" in legacy:
        warnings.warn("testcase_func_doc= is deprecated; use doc_func=",
                      DeprecationWarning, stacklevel=2)
        if not doc_func:
            doc_func = legacy["testcase_func_doc"]

    doc_func = doc_func or default_doc_func
    name_func = name_func or default_name_func

    def parameterized_expand_wrapper(f, instance=None):
        frame_locals = inspect.currentframe().f_back.f_locals

        parameters = parameterized.input_as_callable(input)()

        if not parameters:
            if not skip_on_empty:
                raise ValueError(
                    "Parameters iterable is empty (hint: use "
                    "`parameterized.expand([], skip_on_empty=True)` to skip "
                    "this test when the input is empty)"
                )
            return wraps(f)(skip_on_empty_helper)

        digits = len(str(len(parameters) - 1))
        for num, p in enumerate(parameters):
            name = name_func(f, "{num:0>{digits}}".format(digits=digits, num=num), p)
            # If the original function has patches applied by 'mock.patch',
            # re-construct all patches on the just former decoration layer
            # of param_as_standalone_func so as not to share
            # patch objects between new functions
            nf = reapply_patches_if_need(f)
            frame_locals[name] = parameterized.param_as_standalone_func(p, nf, name)
            frame_locals[name].__doc__ = doc_func(f, num, p)

        # Delete original patches to prevent new function from evaluating
        # original patching object as well as re-constructed patches.
        delete_patches_if_need(f)

        f.__test__ = False
    return parameterized_expand_wrapper

def data_class(attrs,input_values):
    """
    参数化类
    :param attrs:
    :param input_values:
    :return:
    """
    return parameterized_class(attrs,input_values)