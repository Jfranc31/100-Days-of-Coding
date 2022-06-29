fsurf(@(u,v)sin(pi*u).*sin(pi*u).*cos(v), ...
    @(u,v)sin(pi*u).*sin(pi*u).*sin(v), ...
    @(u,v)u, [-1 1 0 2*pi])
title(["$x = \sin(\pi u) \sin(\pi u) \cos(v)$", ...
    "$y = \sin(\pi u) \sin(\pi u) \sin(v)$", ...
    "$z = u$"], ...
    "Interpreter","latex")