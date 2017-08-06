out = []

for i = 1:1000
    fscale = 25000
    fk = [0 fscale 0]'
    tac = mod( randi(100), 3)
    
    switch tac
        % straight
        case 0
            fk = [0 0 0]'
        % left
        case 1
            fk = [0 fscale 0]'
        % right
        case 2
            fk = [0 -fscale 0]'
        otherwise
            warning('Unexpected')
    end
    
    % add up some variance with gaussion distribution
    var = fscale/4
    r = -var + (var+var)*rand(3,1)
    fk =fk+r
    
    %run
    sim('maneuver_generator')
    
    %downsampling, getting 10 time step samles makes a more sparse sample
    %ts1 = getsamples(ts, ts.time([2 3]))
    sample = [ traj.data(:,1), traj.data(:,2), traj.data(:,3), traj.data(:,4), traj.time ]
    out = [out;sample];
end