function getArgs(func)
    local args = {}
    for i = 1, debug.getinfo(func).nparams, 1 do
        table.insert(args, debug.getlocal(func, i));
    end
    return args;
end

function keyat(index,table)
    local i = 1
    for k,_ in pairs(table) do
        if i == index then return k
        else i = i+1 end
    end
    return nil
end


function len(table)
    local c = 0
    for _,v in pairs(table) do c = c+1 end
    return c
end

function tabasstring(obj)
    local out
    if type(obj) == "table" then
        out = "{"
        local k
        for n = 1,len(obj)-1 do
            k = keyat(n,obj)
            out = out..k.." = "..tabasstring(obj[k])..", "
        end
        k = keyat(len(obj),obj)
        out = out..k.." = "..tabasstring(obj[k]).."}"
    else
        out = obj
        if type(obj) == "function" then
            local ags = getArgs(obj)
            local a = ""
            if len(ags) > 0 then
                for n = 1,len(ags)-1 do
                   a = a..ags[n]..", "
                end
                print(ags)
                a = a..ags[len(ags)]
            end
            out = "func("..a..")"
        end
    end
    return out
end

t = {
    name = "fred",
    attack = -1,
    health = 40,
    speed = 1000,
    tab = {one = 2, two = 1, threes = {3,6,9}},
    f1 = function()
        return nil
    end,
    f2 = function(par1,par2)
        return nil
    end
}

print(tabasstring(t))





