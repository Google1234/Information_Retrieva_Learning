
'''
SPIMI-Invert(Token_stream)
output.file=NEWFILE()
dictionary = NEWHASH()
while (free memory available)
    do token <-next(token_stream) //逐一处理每个词项-文档ID对
        if term(token) !(- dictionary
           /*如果词项是第一次出现，那么加入hash词典，同时，建立一个新的倒排索引表*/
           then postings_list = AddToDictionary(dictionary,term(token))
        /*如果不是第一次出现，那么直接返回其倒排记录表，在下面添加其后*/
        else postings_list = GetPostingList(dictionary,term(token))
    if full(postings_list)
        then postings_list =DoublePostingList(dictionary,term(token))
    /*SPIMI与BSBI的区别就在于此，前者直接在倒排记录表中增加此项新纪录*/
    AddToPosTingsList (postings_list,docID(token))
sorted_terms <- SortTerms(dictionary)
WriteBlockToDisk(sorted_terms,dictionary,output_file)
return output_file
'''