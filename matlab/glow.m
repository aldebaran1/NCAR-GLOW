function iono = glow(time, glat, glon, f107a, f107, f107p, Ap, Q, Echar, Nbins)

validateattributes(glat, {'numeric'}, {'scalar'})
validateattributes(glon, {'numeric'}, {'scalar'})
validateattributes(f107, {'numeric'}, {'positive', 'scalar'})
validateattributes(f107a, {'numeric'}, {'positive', 'scalar'})
validateattributes(f107p, {'numeric'}, {'positive', 'scalar'})
validateattributes(Ap, {'numeric'}, {'positive', 'scalar'})
validateattributes(Q, {'numeric'}, {'positive', 'scalar'})
validateattributes(Echar, {'numeric'}, {'positive', 'scalar'})
validateattributes(Nbins, {'numeric'}, {'positive', 'integer', 'scalar'})
%% binary
exe = glowpath();
[idate, utsec] = glowdate(time);

cmd = [exe, ' ', idate,' ',utsec,' ',...
       num2str([glat, glon, f107a, f107, f107p, Ap, Q, Echar, Nbins])];
[status,dat] = system(cmd);
if status ~= 0, error(dat), end

iono = glowparse(dat);
end
