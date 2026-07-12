"use client";
import { Card } from "@/components/ui/card";
import { Pencil, Trash2 } from "lucide-react";
import { Button } from "../ui/button";
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { useSessions } from "@/hooks/useSessions";
import { useRouter } from "next/navigation";

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";


interface SessionCardProps {
  id: string;
  title: string;
  updatedAt: string;
  onClick: () => void;
  isActive: boolean;
}

export function SessionCard({
  id,
  title,
  updatedAt,
  isActive,
  onClick,
}: SessionCardProps) {

  const router = useRouter();
  const [isEditing, setIsEditing] = useState(false);
  const [draftTitle, setDraftTitle] = useState(title);
  const [isDeleteOpen, setIsDeleteOpen] = useState(false);

  const { updateSessionMutation,deleteSessionMutation } = useSessions();

 
async function saveTitle() {
  const trimmed = draftTitle.trim();

  if (!trimmed || trimmed === title) {
    setIsEditing(false);
    setDraftTitle(title);
    return;
  }

  try {
    await updateSessionMutation.mutateAsync({
      sessionId: id,
      data: {
        title: trimmed,
      },
    });

    setIsEditing(false);
  } catch (error) {
    console.error(error);
  }
}

async function handleDelete() {
  try {
    await deleteSessionMutation.mutateAsync(id);

    setIsDeleteOpen(false);

    if (isActive) {
      router.push("/");
    }
  } catch (error) {
    console.error(error);
  }
}

  return (
    <div className="group">
    <Card onClick={onClick} className={`
    cursor-pointer
    px-3 py-2.5
    transition-all duration-200
    ${
    isActive
  ? `
      bg-zinc-800
      border-l-2
      border-l-emerald-500
    `
  : `
      hover:bg-zinc-800/60
    `
    }
  `}>
        <div className="flex items-start gap-2">
        <div className="min-w-0 flex-1">
          {
            isEditing ? (
              <Input
                autoFocus
                value={draftTitle}
                onBlur={saveTitle}
                onChange={(e) => setDraftTitle(e.target.value)}
                onKeyDown={(e) => {
                  e.stopPropagation();
                    if (e.key === "Enter") {
                      e.preventDefault();
                      e.currentTarget.blur();
                    }

                    if (e.key === "Escape") {
                      setDraftTitle(title);
                      setIsEditing(false);
                    }
                  }}
                className="h-7"
              />
            ) : (
              <p className="truncate text-sm font-medium">
                {title}
              </p>
            )
          }

          <p className="mt-1 text-[11px] text-zinc-500">
            {updatedAt}
          </p>

          <div className="flex shrink-0 items-center gap-1 opacity-0 transition-opacity group-hover:opacity-100">
            <Button
            variant="ghost"
            size="icon"
            className="h-7 w-7 text-zinc-400 hover:text-white cursor-pointer"
            onClick={(e) => {
              e.stopPropagation();
              setDraftTitle(title);
              setIsEditing(true);
            }}
          >
          <Pencil className="h-4 w-4" />
          </Button>
          <AlertDialog
  open={isDeleteOpen}
  onOpenChange={setIsDeleteOpen}
>
          <AlertDialogTrigger asChild>
            <Button
              variant="ghost"
              size="icon"
              className="h-7 w-7 cursor-pointer text-zinc-400 hover:text-red-400"
              onClick={(e) => e.stopPropagation()}
            >
              <Trash2 className="h-4 w-4" />
            </Button>
          </AlertDialogTrigger>

          <AlertDialogContent
            onClick={(e) => e.stopPropagation()}
          >
            <AlertDialogHeader>
              <AlertDialogTitle>
                Delete chat?
              </AlertDialogTitle>

              <AlertDialogDescription>
                This conversation and all of its messages will be permanently deleted.
                This action cannot be undone.
              </AlertDialogDescription>
            </AlertDialogHeader>

            <AlertDialogFooter>
              <AlertDialogCancel
                disabled={deleteSessionMutation.isPending}
              >
                Cancel
              </AlertDialogCancel>

              <AlertDialogAction
                disabled={deleteSessionMutation.isPending}
                className="bg-red-600 hover:bg-red-700"
                onClick={(e) => {
                  e.preventDefault();
                  handleDelete();
                }}
              >
                {deleteSessionMutation.isPending
                  ? "Deleting..."
                  : "Delete"}
              </AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>
        </div>
      </div>
    </div>
    </Card>
    </div>
  );
}