
'''
Way1:
    主索引(Main index)+辅助索引(Auxiliary index)
    在磁盘上维护一个大的主索引(Main index)
    新文档放入内存中较小的辅助索引中
    同时搜索两个索引，然后合并结果
    定期将辅助索引合并到主索引中

    删除的处理：
    采用无效位向量(Invalidation bit-vector)来表示删除的文档
    利用该维向量过滤返回的结果，以去掉已删除文档
存在的问题：
    合并过于频繁
    合并时如果正好在搜索，那么搜索的性能将很低
    实际上:
    如果每个倒排记录表都采用一个单独的文件来存储的话，那么将辅助索引合并到主索引的代价并没有那么高
    此时合并等同于一个简单的添加操作
    但是这样做将需要大量的文件，效率显然不高
    如果没有特别说明，本讲后面都假定索引是一个大文件
    现实当中常常介于上述两者之间(例如：将大的倒排记录表分割成多个独立的文件，将多个小倒排记录表存放在一个文件当中……)
'''

'''
Way2:
    对数合并(Logarithmic merge)：
    对数合并算法能够缓解(随时间增长)索引合并的开销
    → 用户并不感觉到响应时间上有明显延迟
    维护一系列索引，其中每个索引是前一个索引的两倍大小
    将最小的索引 (Z0) 置于内存
    其他更大的索引  (I0, I1, . . . ) 置于磁盘
    如果 Z0 变得太大 (> n), 则将它作为 I0 写到磁盘中(如果 I0 不存在)
    或者和 I0 合并(如果 I0 已经存在) ，并将合并结果作为I1写到磁盘中(如果 I1 不存在) ，或者和I1合并(如果 I0 已经存在)，依此类推……
'''