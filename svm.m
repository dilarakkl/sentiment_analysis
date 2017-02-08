svm_option='-t 0 -s 0 -q -b 1';

train = dlmread('all_train2.txt');

train_label = dlmread('label_train.txt');

model=svmtrain(train_label,train,svm_option);

fprintf('TRAIN DONE\n');

test = dlmread('all_test2.txt');

test_label = dlmread('label_test.txt');

[predicted_label, accuracy, decision_values] = svmpredict(test_label, test, model, '-q');

fprintf('ALL DONE\n');
Prediction = []
Prediction=[Prediction predicted_label];
accuracy


C=confusionmat(test_label',predicted_label');
p_pre = C(1,1) / sum(C(:,1));
n_pre = C(2,2) / sum(C(:,2));
neg_pre = C(3,3) / sum(C(:,3));
p_rec = C(1,1) / sum(C(1,:));
n_rec = C(2,2) / sum(C(2,:));
neg_rec = C(3,3) / sum(C(3,:));

total_pre = (p_pre + n_pre + neg_pre)/3;
total_rec = (p_rec + n_rec + neg_rec)/3;
f1 = 2*total_pre*total_rec / (total_pre + total_rec);

for i=1:3
    
    C(i,:)=C(i,:)/sum(C(i,:));
end

imshow(C, 'InitialMagnification',3000)  % # you want your cells to be larger than single pixels
colormap(jet)


