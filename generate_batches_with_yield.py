def generate_batches(data,batchsize,num_epoch,shuffle=True):
    '''
    产生batches 为NN 的输入feed，返回的是一个数据集的迭代器，
    :param data:
    :param batchsize:
    :param num_epoch:
    :param shuffle:
    :return:
    '''
    data=np.asarray(data)
    data_size=len(data)

    batches_per_epoch=int(data_size/batchsize)

    for _  in range(num_epoch):
        if(shuffle):
            shuffle_idx=np.random.permutation(np.arange(data_size))
            shuffled_data=data[shuffle_idx]

        else:
            shuffled_data=data

        for batch_num in range(batches_per_epoch):
            start_index=batch_num
            end_index=min((batch_num+1)*batchsize,data_size)
            yield shuffled_data[start_index:end_index]
            # 这里的yield会返回一个迭代器  ,可以手动返回也可以不显示的返回，他会自动返回
