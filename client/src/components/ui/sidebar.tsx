import * as React from "react";
import { PanelLeft } from "lucide-react";
import { cn } from "@/lib/utils";

const Sidebar = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => (
    <div ref={ref} className={cn("bg-background p-4", className)} {...props} />
));

Sidebar.displayName = "Sidebar";

export { Sidebar };
