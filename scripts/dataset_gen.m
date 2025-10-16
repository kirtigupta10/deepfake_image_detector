% scripts/dataset_gen.m
% Generate synthetic dataset for deepfake image detection
% Requires Image Processing Toolbox

% Number of images per class
numImages = 750; % total 1500

% Folder paths
folderReal = fullfile('dataset', 'real');
folderFake = fullfile('dataset', 'fake');

if ~exist(folderReal, 'dir'), mkdir(folderReal); end
if ~exist(folderFake, 'dir'), mkdir(folderFake); end

imgSize = [128 128 3];

for i = 1:numImages
    % ---------- Real-like images ----------
    imgReal = imgaussfilt(rand(imgSize), randi([1, 3])); % smooth (natural)
    imwrite(imgReal, fullfile(folderReal, sprintf('real_%04d.jpg', i)));

    % ---------- Fake-like images ----------
    imgFake = imsharpen(rand(imgSize), ...
        'Radius', rand*2, 'Amount', rand*2); % extra sharp, unnatural edges
    imgFake = imnoise(imgFake, 'salt & pepper', 0.02 + rand*0.03); % add artifacts
    imwrite(imgFake, fullfile(folderFake, sprintf('fake_%04d.jpg', i)));
end

disp('✅ Dataset of 1500 images generated successfully!');
